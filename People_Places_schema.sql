
drop table if exists places;

create table `places` (
	`City` varchar(100),
	`Country` varchar(100),
	`Provience` varchar(100) NOT NULL,
	primary key (`city`)
);


drop table if exists people;

create table `people` (
	`id` int not null auto_increment,
	`First_Name` varchar(100),
	`Last_Name` varchar(100),
	`DOB` Date,
	`POB` varchar(100),
	primary key (`id`),
	FOREIGN KEY (POB) REFERENCES places(city)	
);	



select places.provience,count(*) from temper_code_test.places places
join temper_code_test.people people 
on places.Provience=people.POB
group bu places.provience;


==================================================
*******Sample Data to test the query***********
==================================================

insert into people values('John','Williams','1842-09-30','Dumfries');
insert into people values('Grace','Jeffery','1899-06-14','Kelso');
insert into people values('Sean','Molnar','1982-11-01','Dromore');
insert into people values('Lily','Doyle','1883-04-02','Hamilton');
insert into people values('Edith','Styles','1879-07-24','Ballymoney');
insert into people values('John','Brown','1892-09-05','Kilmarnock');
insert into people values('Jose','Barth','1942-08-13','Newtownards');
insert into people values('Leonard','Beetham','1897-05-25','Enniskillen');


insert into places(City,Country,Provience) values('Dumfries','Dumfriesshire','Scotland');
insert into places(City,Country,Provience) values('Kelso','Roxburghshire','Scotland');
insert into places(City,Country,Provience) values('Dromore','Down','Northern Ireland');























