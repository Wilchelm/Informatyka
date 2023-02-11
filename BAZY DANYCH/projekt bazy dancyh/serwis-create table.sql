if db_id('serwis_komputerowy') is not null
print 'Baza danych istnieje'
else create database serwis_komputerowy

set language polish

IF OBJECT_ID (N'Pracownicy', N'U') IS NOT NULL 
drop table Pracownicy

create table Pracownicy(
id_prac int primary key, 
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
id_kli int primary key,
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
id_proc int primary key,
nazwa varchar(30) not null
)

IF OBJECT_ID (N'Grafika', N'U') IS NOT NULL 
drop table Grafika

create table Grafika(
id_gpu int primary key,
nazwa varchar(30) not null,
pamiec int not null/*w megabajtach*/
)

IF OBJECT_ID (N'Ram', N'U') IS NOT NULL 
drop table Ram

create table Ram(
wielkosc int primary key/*w megabijtach*/
)

IF OBJECT_ID (N'Dysk', N'U') IS NOT NULL 
drop table Dysk

create table Dysk(
id_rom int primary key,
typ varchar(3) not null,/*SSD albo HDD*/
rozmiar int not null/*w GB*/
)

IF OBJECT_ID (N'OS', N'U') IS NOT NULL 
drop table OS

create table OS(
id_os int primary key,
nazwa varchar(20)not null
)

IF OBJECT_ID (N'Komputer', N'U') IS NOT NULL 
drop table Komputer

create table Komputer(
id_urz int primary key,
typ varchar(30) not null,/*pc,laptop*/
cpu int references Procesor(id_proc),
gpu int references Grafika(id_gpu),
ram int references Ram(wielkosc),
rom int references Dysk(id_rom),
os int references OS(id_os),
wielkosc_matrycy varchar(4),/*np 17,3"*/
wartosc money not null
)


if OBJECT_ID(N'Cennik',N'U') is not null
drop table Cennik

create table Cennik(
nazwa_czynnosci varchar(30) primary key,
cena money not null
)

if OBJECT_ID(N'Zgloszenie',N'U') is not null
drop table Zgloszenie

create table Zgloszenie(
id int primary key,
kto int references Klienci(id_kli),
naprawa varchar(30) references Cennik(nazwa_czynnosci) ,
aktualny_stan varchar(30) not null /*przyjeto, realizacja, gotowe do odbioru, odebrano*/
)

insert into Pracownicy
values(1, 'Andrzej' , 'M≥ot' , 'ul.Nowa 4', '12-145 Warszawa','123456789', 'mlot@gmail.com', 'kierownik');
insert into Pracownicy
values(2, 'Marcin' , 'Nowak' , 'ul.DÍbowa 4', '61-512 £Ûdü','120753801', 'nowak@gmail.com', 'obs≥uga klienta');
insert into Pracownicy
values(3, 'Magda' , 'B≥aszczyk' , 'ul.Wilcza 5', '62-681 Nowa Wieú','986308625', 'blaszczyk@gmail.com', 'obs≥uga klienta');
insert into Pracownicy
values(4, 'Adam' , 'Chmielnicki' , 'ul.Starej daty 8', '74-288 Ko≥obrzeg','633678789', 'chmielnicki@gmail.com', 'serwisant');
insert into Pracownicy
values(5, 'Monika' , 'Zielona' , 'ul.Mokra 13', '74-704 Szczecin','120976689', 'zielona@gmail.com', 'serwisant');

insert into Klienci
values(1,'Al', 'Takt', 'ul.Nowej Ziemi 38', '24-515 Warszawa','758930287','takt@gmail.com');
insert into Klienci
values(2,'Adam', 'Adamczak', 'ul.Ptasia 28', '72-516 Szczecin','348930287','adamczak@gmail.com');
insert into Klienci
values(3,'Bartosz', 'Lewandowski', 'ul.Lisia 15', '63-673 Nowa Wieú','787630287','lewandowski@gmail.com');
insert into Klienci
values(4,'Rafa≥', 'Unok', 'ul.Sokola 38', '24-515 Warszawa','568930287','unok@gmail.com');
insert into Klienci
values(5,'Fred', 'Taczak', 'ul.Ruda 49', '24-515 S≥Ûj','758762087','taczak@gmail.com');

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
values(1,'Intel I3');
insert into Procesor
values(2,'Intel I5');
insert into Procesor
values(3,'Intel I7');

insert into Dysk
values(1,'HDD',500);
insert into Dysk
values(2,'HDD',1000);
insert into Dysk
values(3,'HDD',2000);
insert into Dysk
values(4,'SSD',120);
insert into Dysk
values(5,'SSD',240);
insert into Dysk
values(6,'SSD',480);

insert into Grafika
values(1,'AMD 7970',3072);
insert into Grafika
values(2,'AMD 7850',2048);
insert into Grafika
values(3,'Nvidia 770',2048);
insert into Grafika
values(4,'Nvidia 780',4096);
insert into Grafika
values(5,'Intel HD', 1024);

insert into OS
values(1,'brak systemu');
insert into OS
values(2,'Windows 10');
insert into OS
values(3,'Windows 8.1');
insert into OS
values(4,'Ubuntu');

insert into Komputer
values(1,'pc',1,2,2048,1,1,'',2000);
insert into Komputer
values(2,'pc',3,2,4096,4,2,'',2500);
insert into Komputer
values(3,'pc',3,4,8192,2,1,'',5000);
insert into Komputer
values(4,'laptop',1,5,4096,1,2,'13,3',1600);
insert into Komputer
values(5,'laptop',1,5,2048,2,3,'17,3',1800);
insert into Komputer
values(6,'laptop',2,5,8192,5,2,'15,6',2800);

insert into Cennik
values('instalacja systemu',50);
insert into Cennik
values('instalacja ch≥odzenia',80);
insert into Cennik
values('sk≥adanie komputera',300);
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
values(1,1,'wymiana grafiki','gotowe do odbioru');
insert into Zgloszenie
values(2,1,'wymiana procesora','gotowe do odbioru');
insert into Zgloszenie
values(3,1,'instalacja systemu','realizacja');
insert into Zgloszenie
values(4,3,'wymiana grafiki','gotowe do odbioru');
insert into Zgloszenie
values(5,2,'sk≥adanie komutera','gotowe do odbioru');
insert into Zgloszenie
values(6,4,'instalacja systemu','gotowe do odbioru');
insert into Zgloszenie
values(7,2,'odzyskiwanie danych','realizacja');
