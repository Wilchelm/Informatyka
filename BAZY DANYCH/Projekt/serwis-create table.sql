if db_id('serwis_komputerowy') is not null
print 'Baza danych istnieje'
else create database serwis_komputerowy

use serwis_komputerowy

set language polish

IF OBJECT_ID (N'Pracownicy', N'U') IS NOT NULL 
drop table Pracownicy

create table Pracownicy(
id_prac int identity(1,1) primary key, 
imie varchar(20)not null,
nazwisko varchar(20)not null,
adres varchar(30)not null,/* nazwa ulicy numer domu*/
miasto  varchar(30)not null, /*kod pocztowy miasto*/
telefon varchar(9),
mail  varchar(50),
stanowisko  varchar(30)not null
)

IF OBJECT_ID (N'Klienci', N'U') IS NOT NULL 
drop table Klienci

create table Klienci(
id_kli int identity(1,1) primary key,
imie varchar(20)not null,
nazwisko varchar(20)not null,
adres varchar(30)not null,/* nazwa ulicy numer domu*/
miasto  varchar(30)not null, /*kod pocztowy miasto*/
telefon varchar(9),
mail  varchar(50)
)
IF OBJECT_ID (N'Procesor', N'U') IS NOT NULL 
drop table Procesor

create table Procesor(
id_proc int identity(1,1) primary key,
nazwa varchar(30) not null
)

IF OBJECT_ID (N'Grafika', N'U') IS NOT NULL 
drop table Grafika

create table Grafika(
id_gpu int identity(1,1) primary key,
nazwa varchar(30) not null,
pamiec int not null/*w megabajtach*/
)

IF OBJECT_ID (N'Ram', N'U') IS NOT NULL 
drop table Ram

create table Ram(
id_ram int identity(1,1) primary key,
wielkosc int,
)

if object_ID (N'Statusy', N'U') is not null
drop table Statusy

create table Statusy(
id_stat int identity(1,1) primary key,
nazwa varchar (20)
)

IF OBJECT_ID (N'Dysk', N'U') IS NOT NULL 
drop table Dysk

create table Dysk(
id_rom int identity(1,1) primary key,
typ varchar(3) not null,/*SSD albo HDD*/
rozmiar int not null/*w GB*/
)

IF OBJECT_ID (N'OS', N'U') IS NOT NULL 
drop table OS

create table OS(
id_os int identity(1,1) primary key,
nazwa varchar(20)not null
)

IF OBJECT_ID (N'Komputer', N'U') IS NOT NULL 
drop table Komputer

create table Komputer(
id_urz int identity(1,1) primary key,
typ varchar(30) not null,/*pc,laptop*/
cpu int references Procesor(id_proc),
gpu int references Grafika(id_gpu),
ram int references Ram(id_ram),
rom int references Dysk(id_rom),
os int references OS(id_os),
wielkosc_matrycy varchar(4),/*np 17,3"*/
wartosc money not null
)


if OBJECT_ID(N'Cennik',N'U') is not null
drop table Cennik

create table Cennik(
id_cen int identity(1,1) primary key,
nazwa_czynnosci varchar(30),
cena money not null
)

if OBJECT_ID(N'Zgloszenie',N'U') is not null
drop table Zgloszenie

create table Zgloszenie(
id int identity(1,1) primary key,
kto int references Klienci(id_kli),
kto_naprawia int foreign key references Pracownicy(id_prac),
naprawa varchar(30),
aktualny_stan int references Statusy(id_stat) /*przyjeto, realizacja, gotowe do odbioru, odebrano*/
)

insert into Pracownicy
values('Andrzej' , 'Mlot' , 'ul.Nowa 4', '12-145 Warszawa','123456789', 'mlot@mail.com', 'kierownik');
insert into Pracownicy
values('Marcin' , 'Nowak' , 'ul.Debowa 4', '61-512 Lodz','120753801', 'nowak@mail.com', 'obsluga klienta');
insert into Pracownicy
values('Magda' , 'Blaszczyk' , 'ul.Wilcza 5', '62-681 Nowa Wies','986308625', 'blaszczyk@mail.com', 'obsluga klienta');
insert into Pracownicy
values('Adam' , 'Chmielnicki' , 'ul.Starej daty 8', '74-288 Kolobrzeg','633678789', 'chmielnicki@mail.com', 'serwisant');
insert into Pracownicy
values('Monika' , 'Zielona' , 'ul.Mokra 13', '74-704 Szczecin','120976689', 'zielona@mail.com', 'serwisant');

insert into Klienci
values('Al', 'Takt', 'ul.Nowej Ziemi 38', '24-515 Warszawa','758930287','takt@mail.com');
insert into Klienci
values('Adam', 'Adamczak', 'ul.Ptasia 28', '72-516 Szczecin','348930287','adamczak@mail.com');
insert into Klienci
values('Bartosz', 'Lewandowski', 'ul.Lisia 15', '63-673 Nowa Wies','787630287','lewandowski@mail.com');
insert into Klienci
values('Rafal', 'Unok', 'ul.Sokola 38', '24-515 Warszawa','568930287','unok@mail.com');
insert into Klienci
values('Fred', 'Taczak', 'ul.Ruda 49', '24-515 Sloj','758762087','taczak@mail.com');

insert into Ram
values(1024); 
insert into Ram
values(2048);
insert into Ram
values(4096);
insert into Ram
values(8192);
insert into Ram
values(16384);

insert into Procesor
values('Intel I3');
insert into Procesor
values('Intel I5');
insert into Procesor
values('Intel I7');

insert into Dysk
values('HDD',500);
insert into Dysk
values('HDD',1000);
insert into Dysk
values('HDD',2000);
insert into Dysk
values('SSD',120);
insert into Dysk
values('SSD',240);
insert into Dysk
values('SSD',480);

insert into Grafika
values('AMD 7970',3072);
insert into Grafika
values('AMD 7850',2048);
insert into Grafika
values('Nvidia 770',2048);
insert into Grafika
values('Nvidia 780',4096);
insert into Grafika
values('Intel HD', 1024);

insert into OS
values('brak systemu');
insert into OS
values('Windows 10');
insert into OS
values('Windows 8.1');
insert into OS
values('Ubuntu');

insert into Statusy
values('przyjeto');
insert into Statusy
values('realizacja');
insert into Statusy
values('gotowe do odbioru');
insert into Statusy
values('odebrano');

insert into Komputer
values('pc',1,2,1,1,1,'',2000);
insert into Komputer
values('pc',3,2,2,4,2,'',2500);
insert into Komputer
values('pc',3,4,3,2,1,'',5000);
insert into Komputer
values('laptop',1,5,2,1,2,'13,3',1600);
insert into Komputer
values('laptop',1,5,1,2,3,'17,3',1800);
insert into Komputer
values('laptop',2,5,3,5,2,'15,6',2800);

insert into Cennik
values('instalacja systemu',50);
insert into Cennik
values('instalacja chlodzenia',80);
insert into Cennik
values('skladanie komputera',300);
insert into Cennik
values('wymiana ram',10);
insert into Cennik
values('wymiana grafiki',60);
insert into Cennik
values('wymiana procesora',120);
insert into Cennik
values('odzyskiwanie danych',150);
insert into Cennik
values('odwirusowywanie',80);

insert into Zgloszenie
values(1,1,'wymiana grafiki',3);
insert into Zgloszenie
values(2,1,'wymiana procesora',3);
insert into Zgloszenie
values(3,1,'instalacja systemu',2);
insert into Zgloszenie
values(4,3,'wymiana grafiki',3);
insert into Zgloszenie
values(5,2,'skladanie komputera',3);
insert into Zgloszenie
values(3,4,'instalacja systemu',1);
insert into Zgloszenie
values(3,2,'odzyskiwanie danych',4);
