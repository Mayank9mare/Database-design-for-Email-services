create database Emaildatabase;

show databases;
use emaildatabase;

show tables;
create table userinfo(
	emailid varchar(60) not null primary key,
    passwd varchar(60) not null,
    fname varchar(40),
    lname varchar(40),
    country varchar(40),
    phonenum varchar(30),
    totalmails int,
    age int,
    activemails int
);

-- alter table userinfo
-- add activemails int;

create table inbox (
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
    mailno int,
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);

create table trash (
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);

create table allmails(
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
    mailno int,
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);


-- create table archieved(
-- 	from_eid varchar(60) not null,
--     to_eid varchar(60) not null,
--     tmstp timestamp not null,
--     subj varchar(30),
--     mailcontent varchar(1000),
-- 	foreign key (from_eid) references userinfo(emailid),
--     foreign key (to_eid) references userinfo(emailid)
-- );
create table sent(
	from_eid varchar(60) not null,
    to_eid varchar(60) not null,
    tmstp timestamp not null,
    subj varchar(30),
    mailcontent varchar(1000),
	foreign key (from_eid) references userinfo(emailid),
    foreign key (to_eid) references userinfo(emailid)
);

insert into userinfo values('nirbhaysharma@gmail.com','password','nirbhay','sharma','india','9999999999',0,26,0);
insert into userinfo values('nirbhaysharma@gmail.dom','password','nirbhay','sharma','india','9999999991',0,26,0);
select * from userinfo;
select * from userinfo where emailid = 'nirbhaysharma@gmail.com', passwd= 'password';
drop table allmails;
drop table inbox;
drop table sent;
-- drop table archieved;
drop table trash;
drop table userinfo;
truncate table userinfo;

DELIMITER $$
CREATE TRIGGER sent_trigger
after insert
ON sent
for each row
BEGIN
    insert into allmails values (new.from_eid,new.to_eid,new.tmstp,new.subj,new.mailcontent,1+(select totalmails from userinfo where emailid=new.to_eid));
    insert into inbox values (new.from_eid,new.to_eid,new.tmstp,new.subj,new.mailcontent,1+(select totalmails from userinfo where emailid=new.to_eid));
    update userinfo set totalmails = totalmails + 1, activemails= activemails+1 where emailid = new.to_eid;
END $$
DELIMITER ;

INSERT INTO sent values('nirbhaysharma@gmail.com','gauri@gmail.com',CURRENT_TIMESTAMP,'regarding hi','hello my name is nirbhay sharma');

drop trigger sent_trigger;
drop trigger inbox_trigger;
describe userinfo;

DELIMITER $$ 
create trigger inbox_trigger
AFTER delete
on inbox
for each row
BEGIN
    INSERT INTO trash VALUES(old.from_eid,old.to_eid,old.tmstp,old.subj,old.mailcontent);
    update userinfo set activemails = activemails - 1 where emailid = old.to_eid;
END $$
DELIMITER ;

delete from inbox where to_eid='gauri@gmail.com' and mailno=1;

select * from inbox;
select * from allmails;
select * from userinfo;
select * from sent;
select * from trash;

