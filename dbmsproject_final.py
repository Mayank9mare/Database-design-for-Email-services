# first we create login and register system
from tkinter import *
# import os
import tkinter.messagebox as msg
import re,random,string,datetime
# os.system("pip install mysql-connector-python")

import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd = "1234",database="emaildatabase")
mycursor = mydb.cursor()


def login():
    def handlelogin(eml,fnam,lnam):
        def showinbox():
            global mycursor;
            mycursor.execute(f"select * from inbox where to_eid = '{eml}'");
            ll = []
            for i in mycursor:
                ll.append(i)
            for widgets in frame2.winfo_children():
                widgets.destroy()

            mylistbox = Listbox(frame2,height=frame2.winfo_screenheight(),width=frame2.winfo_screenwidth())
            mylistbox.pack();
            index = 1;
            if (len(ll) == 0):
                mylistbox.insert(index,"  nothing to show up here");
            else:
                for j in range(len(ll)):
                    i = ll[j]
                    mylist[j+1] = i[-1]
                    val1 = f"{j+1}. from: {i[0]}"
                    val2 = f"  recieved at: {i[2]}"
                    val3 = f"  subject: {i[3]}\n"
                    val4 = f"  content: {i[4]}"
                    mylistbox.insert(index,val1)
                    index += 1
                    mylistbox.insert(index,val2)
                    index += 1
                    mylistbox.insert(index,val3)
                    index += 1
                    mylistbox.insert(index,val4)
                    index += 1
                    mylistbox.insert(index, " ")
                    index += 1

        def showsent():
            global mycursor;
            mycursor.execute(f"select * from sent where from_eid = '{eml}'");
            ll = []
            for i in mycursor:
                ll.append(i)
            for widgets in frame2.winfo_children():
                widgets.destroy()
            mylistbox = Listbox(frame2,height=frame2.winfo_screenheight(),width=frame2.winfo_screenwidth())
            mylistbox.pack();
            index = 1;
            if (len(ll) == 0):
                mylistbox.insert(index,"  nothing to show up here");
            else:
                for i in ll:
                    val1 = f"  to: {i[1]}"
                    val2 = f"  send at: {i[2]}"
                    val3 = f"  subject: {i[3]}\n"
                    val4 = f"  content: {i[4]}"
                    mylistbox.insert(index,val1)
                    index += 1
                    mylistbox.insert(index,val2)
                    index += 1
                    mylistbox.insert(index,val3)
                    index += 1
                    mylistbox.insert(index,val4)
                    index += 1
                    mylistbox.insert(index, " ")
                    index += 1

        def showtrash():
            global mycursor;
            mycursor.execute(f"select * from trash where to_eid = '{eml}'");
            ll = []
            for i in mycursor:
                ll.append(i)
            for widgets in frame2.winfo_children():
                widgets.destroy()
            
            mylistbox = Listbox(frame2,height=frame2.winfo_screenheight(),width=frame2.winfo_screenwidth())
            mylistbox.pack();
            index = 1;
            if (len(ll) == 0):
                mylistbox.insert(index,"  nothing to show up here");
            else:
                for i in ll:
                    val1 = f"  from: {i[0]}"
                    val2 = f"  recieved at: {i[2]}"
                    val3 = f"  subject: {i[3]}\n"
                    val4 = f"  content: {i[4]}"
                    mylistbox.insert(index,val1)
                    index += 1
                    mylistbox.insert(index,val2)
                    index += 1
                    mylistbox.insert(index,val3)
                    index += 1
                    mylistbox.insert(index,val4)
                    index += 1
                    mylistbox.insert(index, " ")
                    index += 1
        def showallmail():
            global mycursor;
            mycursor.execute(f"select * from allmails where to_eid = '{eml}'");
            ll = []
            for i in mycursor:
                ll.append(i)
            for widgets in frame2.winfo_children():
                widgets.destroy()

            mylistbox = Listbox(frame2,height=frame2.winfo_screenheight(),width=frame2.winfo_screenwidth())
            mylistbox.pack();
            index = 1;
            if (len(ll) == 0):
                mylistbox.insert(index,"  nothing to show up here");
            else:
                for i in ll:
                    val1 = f"  from: {i[0]}"
                    val2 = f"  recieved at: {i[2]}"
                    val3 = f"  subject: {i[3]}\n"
                    val4 = f"  content: {i[4]}"
                    mylistbox.insert(index,val1)
                    index += 1
                    mylistbox.insert(index,val2)
                    index += 1
                    mylistbox.insert(index,val3)
                    index += 1
                    mylistbox.insert(index,val4)
                    index += 1
                    mylistbox.insert(index, " ")
                    index += 1

        def sentmail():
            def sendmail():
                receml = txt1.get("1.0",END).strip();
                subj = txt2.get("1.0",END).strip();
                content = txt3.get("1.0",END).strip();
                global mycursor,mydb;

                mycursor.execute(f"select * from userinfo where emailid='{receml}'")
                c = 0
                for i in mycursor:
                    c+=1
                if (c == 0):
                    msg.showinfo("incorrect email","email address not valid")
                else :
                    mycursor.execute(f"insert into sent values('{eml}','{receml}',CURRENT_TIMESTAMP,'{subj}','{content}')")
                    mydb.commit();
                    root3.destroy();
                    msg.showinfo("sent successful","email send successfully")

            # global root2
            root3 = Toplevel(root2,bg='white')
            root3.title("send email")
            root3.geometry("500x500")
            root3.resizable(0,0)
            scrlbar = Scrollbar(root3)
            scrlbar.pack(side=RIGHT,fill=Y)
            txt1 = Text(root3, height = 3, width = root3.winfo_screenwidth(),yscrollcommand=scrlbar.set)
            txt1.pack()
            txt2 = Text(root3, height = 3, width = root3.winfo_screenwidth(),yscrollcommand=scrlbar.set)
            txt2.pack()
            txt3 = Text(root3, height = 20, width = root3.winfo_screenwidth(),yscrollcommand=scrlbar.set)
            txt3.pack()
            txt1.insert(END,"enter receiver email")
            txt2.insert(END,"subject")
            # txt1.insert(END,"")
            Button(root3, text="Send Mail", fg="white",bg='#4285F4', font=("Comic sans ms", 12), 
            command=sendmail,borderwidth=2, relief=RAISED).pack(pady=5,padx=8)

            scrlbar.config(command=Text.yview)

            root3.mainloop();
            
        def deletemail():
            dells = mylist
            def deleteselect():
                mailno = entry21.get().strip();
                # print(mailno)
                # print(dells)
                if (not mailno.isdigit()):
                    msg.showinfo("error","mail number can only be integer")
                elif (int(mailno) not in dells):
                    msg.showinfo("error","the number with this mail number does not exist");
                else:
                    global mycursor,mydb;
                    mycursor.execute(f"delete from inbox where to_eid='{eml}' and mailno = {dells[int(mailno)]}")
                    mydb.commit();
                    msg.showinfo("success","mail deleted successfully");
                    root4.destroy()
            
            root4 = Toplevel(root2,bg='white')
            root4.title("Delete mails")
            root4.geometry("310x130")
            root4.resizable(0, 0)

            # global entry200
            Label(root4,text="Mail Num:",bg='white',font='lucida 12').grid(row=0,column=0,pady=(10,10))            
            entry21 = Entry(root4,font="lucida 12", borderwidth=2, relief=SUNKEN)
            entry21.grid(row=0,column=1,pady=(10,10))
            # entry200.set("enter mail Number to delete")

            Button(root4, text="Delete", fg="white",bg='#4285F4', font=("Comic sans ms", 12), command=deleteselect,
            borderwidth=2, relief=RAISED).grid(row=1,column=0,columnspan=1,padx=20)


            root4.mainloop();
            
        root2 = Tk()
        root2.title("email system")
        root2.geometry("520x520")

        root2.resizable(0,0)
        # root2 = Toplevel(root1)
        # root2.title("login here")
        # root2.geometry("464x254")
        # root2.resizable(0, 0)
        frame1 = Frame(root2)
        frame1.pack(side=LEFT)
        frame2 = Frame(root2)
        frame2.pack(side=LEFT)

        # scrolbar = Scrollbar(frame2,orient=HORIZONTAL)
        # scrolbar.pack(side=BOTTOM,fill=X)
        Label(frame1,text=f"name:{fnam} {lnam}\nemail:{eml}",fg="blue").pack()
        # mylistbox1 = Listbox(frame1,width=8)
        # mylistbox1.pack();
        # mylistbox1.insert(1,f"name:{fnam} {lnam}")
        # mylistbox1.insert(2,f"")
        Button(frame1, text="Compose", bg="white",fg='#4285F4', font=("Comic sans ms", 12), command=sentmail,
           borderwidth=2, relief=RAISED).pack(pady=5,padx=8)
        Button(frame1, text="Inbox", bg="white",fg='#4285F4', font=("Comic sans ms", 12), command=showinbox,
           borderwidth=2, relief=RAISED).pack(pady=5,padx=8)
        Button(frame1, text="Sent Mails", bg="white",fg='#4285F4', font=("Comic sans ms", 12), command=showsent,
           borderwidth=2, relief=RAISED).pack(pady=5, padx=8)
        Button(frame1, text="Trash", bg="white",fg='#4285F4', font=("Comic sans ms", 12), command=showtrash,
           borderwidth=2, relief=RAISED).pack(pady=5, padx=8)
        Button(frame1, text="All Mails", bg="white",fg='#4285F4', font=("Comic sans ms", 12), command=showallmail,
           borderwidth=2, relief=RAISED).pack(pady=5,padx=8)

        mylist = {}
        
        
        
        global mycursor;
        mycursor.execute(f"select * from inbox where to_eid = '{eml}'");
        ll = []
        for i in mycursor:
            ll.append(i)

        for widgets in frame2.winfo_children():
            widgets.destroy()
        mylistbox = Listbox(frame2,height=frame2.winfo_screenheight(),width=frame2.winfo_screenwidth())
        mylistbox.pack();
        # scrolbar.config(command=mylistbox.xview)
        index = 1;
        if (len(ll) == 0):
            mylistbox.insert(index,"  nothing to show up here");
        else:
            for j in range(len(ll)):
                i = ll[j]
                mylist[j+1] = i[-1]
                val1 = f"{j+1}. from: {i[0]}"
                val2 = f"  recieved at: {i[2]}"
                val3 = f"  subject: {i[3]}\n"
                val4 = f"  content: {i[4]}"
                mylistbox.insert(index,val1)
                index += 1
                mylistbox.insert(index,val2)
                index += 1
                mylistbox.insert(index,val3)
                index += 1
                mylistbox.insert(index,val4)
                index += 1
                mylistbox.insert(index, " ")
                index += 1

        Button(frame1, text="Delete Mails", fg="white",bg='#4285F4', font=("Comic sans ms", 12), command=deletemail,
           borderwidth=2, relief=RAISED).pack(pady=5,padx=8)

        # scrolbar.config(command=Label.yview)

        # Label(frame1, text=f"HI {eml} {fnam} {lnam}", font="lucida 10",fg="black").pack(side=LEFT, anchor='n',pady=25)

        root2.mainloop();
    

    def letmein():
        if any([entry10.get() == "", entry20.get() == ""]):
            msg.showinfo("empty input", "please fill the entries carefully")
            resetkardo()
        else:
            global mycursor,mydb;
            mycursor.execute(f"select * from userinfo where emailid='{entry10.get().strip()}' and passwd='{entry20.get().strip()}'")
            l = []
            for i in mycursor:
                l.append(i)
            if (len(l) == 0):
                    msg.showinfo("error","user does not exist try again")
                    resetkardo()
            else:
                msg.showinfo("Login successful",f"hello {l[0][2]} {l[0][3]}")
                root1.destroy()
                resetkardo();
                handlelogin(l[0][0],l[0][2],l[0][3]);

    def resetkardo():
        entry10.set("")
        entry20.set("")
        # entry30.set("")

    root1 = Toplevel(root,bg='white')
    root1.title("login here")
    root1.geometry("500x254")
    root1.resizable(0, 0)
    frame1 = Frame(root1,bg='white')
    frame1.pack(fill=BOTH)

    # frame = Frame(frame1)
    # frame.pack()

    Label(frame1, text="Email ID:", font="lucida 14",fg="black",bg='white').grid(row=0,column=0,padx=(70,0),pady=(12,10))
    entry10 = StringVar()

    entry1 = Entry(frame1, font="lucida 14", borderwidth=2, relief=SUNKEN, textvariable=entry10)
    # entry1.insert(0,'enter username')
    entry1.grid(row=0,column=1)

    # frame2 = Frame(frame1)
    # frame2.pack()

    Label(frame1, text="Password:", font="lucida 14", fg="black",bg='white').grid(padx= (70,0),row=1,column=0)
    entry20 = StringVar()

    entry2 = Entry(frame1, textvariable=entry20, font="lucida 14", borderwidth=2, relief=SUNKEN)
    entry2.grid(row=1,column=1)

    # frame3 = Frame(frame1)
    # frame3.pack()

    Button(frame1, text="Login", fg="white",bg='#4285F4', font=("Comic sans ms", 14), command=letmein,
           borderwidth=1, relief=RAISED).grid(padx=(80,0),pady=(30,0),row=2,column=0)
    Button(frame1, text="Reset",fg="white",bg='#4285F4', font=("Comic sans ms", 14), command=resetkardo,
           borderwidth=1, relief=RAISED).grid(pady=(30,0),row=2,column=1)
    Button(frame1, text="Exit", fg="white",bg='#4285F4', font=("Comic sans ms", 14), borderwidth=1,
           relief=RAISED, command=root1.destroy).grid(pady=(30,0),row=2,column=2)
    
    root1.mainloop()

    
def signup():
    def validateemail(email):
        reg = r"^[_a-zA-Z0-9-+][_a-zA-Z0-9-.]*?[a-zA-Z0-9]+?@[a-zA-Z0-9-]{1,}?\.([a-zA-Z]{2,3}$|[a-zA-Z]{2,3}\.[a-zA-Z]{2,3}$)"
        reg2 =r"\.{2,}"
        if re.search(reg, email) and not re.search(reg2,email):
            return True
        return False

    def signupkaro():
        if any([entry110.get() == "", entry210.get() == "", entry310.get() == "",
                entry410.get() == "",entry510.get()=="",entry610.get()=="",entry710.get()==""]) or entry510.get().isdigit() == False or len(entry510.get()) != 10 or entry710.get().isdigit()==False:
            msg.showinfo("error in entry", "please fill the entries carefully")
            resetall()
        elif validateemail(entry310.get())==False:
            msg.showinfo("wrong email","please enter a valid email")
            entry310.set("")

        elif any([entry110.get() == "", entry210.get() == "", entry310.get() == "",
                  entry410.get() == "",entry510.get()=="",entry610.get()=="",entry710.get()==""]) == False and entry510.get().isdigit() and len(entry510.get()) == 10 and entry710.get().isdigit()==True:

            
            myemail = entry310.get().strip()
            global mycursor,mydb
            mycursor.execute(f"select * from userinfo where emailid='{myemail}'")
            check = 0
            for i in mycursor:
                check+=1
            if (check == 0):
                mycursor.execute(f"insert into userinfo values('{entry310.get()}','{entry410.get()}','{entry110.get()}','{entry210.get()}','{entry610.get()}','{entry510.get()}',{0},{int(entry710.get().strip())},{0})")
                mydb.commit()
                msg.showinfo("success","sign up successfull")
                root1.destroy()
            else:         
                msg.showinfo("sign up", "please have unique credentials")
            

    def resetall():
        entry110.set("")
        entry210.set("")
        entry310.set("")
        entry410.set("")
        entry510.set("")
        entry610.set("")
        entry710.set("")

    root1 = Toplevel(root,bg='white')
    root1.title("signup here")
    root1.geometry("570x380")
    root1.resizable(0, 0)
    frame1 = Frame(root1,bg='white')
    frame1.pack(fill=BOTH)

    # frame2 = Frame(frame1)
    # frame2.pack()

    Label(frame1, text="First Name:", font="lucida 13", fg="black",bg='white', justify=LEFT).grid(padx=(130,0),row=0,column=0,pady=(40,0))
    entry110 = StringVar()
    entry1 = Entry(frame1, font="lucida 13", borderwidth=2, relief=SUNKEN, textvariable=entry110,width=25)
    entry1.grid(row=0,column=1,pady=(40,5))

    # frame4 = Frame(frame1)
    # frame4.pack()

    Label(frame1, text="Last Name:", font="lucida 13",fg="black",bg='white', justify=LEFT).grid(padx=(130,0),row=1,column=0)
    entry210 = StringVar()
    entry2 = Entry(frame1, font="lucida 13", borderwidth=2, relief=SUNKEN, textvariable=entry210,width=25)
    entry2.grid(row=1,column=1,pady=5)

    # frame5 = Frame(frame1)
    # frame5.pack()

    Label(frame1, text="Email addr: ", font="lucida 13",fg="black",bg='white',justify=LEFT).grid(padx=(130,0),row=2,column=0)
    entry310 = StringVar()
    entry3 = Entry(frame1, font="lucida 13", borderwidth=2, relief=SUNKEN, textvariable=entry310,width=25)
    entry3.grid(row=2,column=1,pady=5)

    # frame6 = Frame(frame1)
    # frame6.pack()

    Label(frame1, text="Password: ", font="lucida 13",fg="black",bg='white',justify=LEFT).grid(padx=(130,0),row=3,column=0)
    entry410 = StringVar()
    entry4 = Entry(frame1, font="lucida 13", borderwidth=2, relief=SUNKEN, textvariable=entry410,width=25)
    entry4.grid(row=3,column=1,pady=5)


    # frame9 = Frame(frame1)
    # frame9.pack()

    Label(frame1, text="Phone num:", font="lucida 13",fg="black",bg='white',justify=LEFT).grid(padx=(130,0),row=4,column=0)
    entry510 = StringVar()
    entry5 = Entry(frame1, font="lucida 13", borderwidth=2, relief=SUNKEN, textvariable=entry510,width=25)
    entry5.grid(row=4,column=1,pady=5)
    
    # frame7 = Frame(frame1)
    # frame7.pack()

    Label(frame1, text="Country:  ", font="lucida 13",fg="black",bg='white',justify=LEFT).grid(padx=(130,0),row=5,column=0)
    entry610 = StringVar()
    entry6 = Entry(frame1, font="lucida 13", borderwidth=2, relief=SUNKEN, textvariable=entry610,width=25)
    entry6.grid(row=5,column=1,pady=5)

    # frame8 = Frame(frame1)
    # frame8.pack()

    Label(frame1, text="Your Age: ", font="lucida 13",fg="black",bg='white',justify=LEFT).grid(padx=(130,0),pady=(5,30),row=6,column=0)
    entry710 = StringVar()
    entry7 = Entry(frame1, font="lucida 13", borderwidth=2, relief=SUNKEN, textvariable=entry710,width=25)
    entry7.grid(row=6,column=1,pady=(5,30))

    # frame3 = Frame(frame1)
    # frame3.pack()

    Button(frame1, text="Signup",fg="white",bg='#4285F4', font=("Comic sans ms", 14), command=signupkaro,
           borderwidth=1, relief=RAISED).grid(padx=(100,0),row=7,column=0)
    Button(frame1, text="Reset",fg="white",bg='#4285F4', font=("Comic sans ms", 14), command=resetall,
           borderwidth=1, relief=RAISED).grid(row=7,column=1)
    Button(frame1, text="EXIT",fg="white", bg='#4285F4',font=("Comic sans ms", 14), borderwidth=1,
           relief=RAISED, command=root1.destroy).grid(row=7,column=2)
    root1.mainloop()


root = Tk()
root.title("login and register system")
root.geometry("500x350")
root.resizable(0,0)

frame = Frame(root,borderwidth=2,relief=RAISED,bg='white')
frame.pack(fill=BOTH)

lab = Label(frame,text="Welcome to the email services\nlogin if you already have an account else register",bg='white',font="lucida 15 bold",fg="#4285F4")
lab.pack(pady=20)

b1 = Button(frame,text="LOGIN",fg="#4285F4",bg='white',pady=10,padx=10,font=("Hack", 14, "bold"),command=login)
b1.pack(pady=10)

b2 = Button(frame,text="REGISTER",fg="white",bg='#4285F4',pady=10,padx=10,font=("Hack" ,14, "bold"),command=signup)
b2.pack(pady=10)

lab1 = Label(frame,text="System by Nirbhay Mayank Kshitiz",font="lucida 15 bold",fg="green",bg='white')
lab1.pack(pady=20)

root.mainloop()



# D:/visual studio code/tkinterprojectsinpython/