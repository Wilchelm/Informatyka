CREATE DATABASE LIGA

CREATE TABLE Kluby (
symbol varchar(8) primary key,
nazwa varchar(20) not null unique, 
miasto varchar(20), 
rok_utworzenia date default getdate(),
trener varchar(20)
)

CREATE TABLE Zawodnicy (
id_zaw int identity(1,1) primary key,
nazwisko varchar(20),
wiek int CHECK (wiek > 18),
kraj varchar(20) default 'Polska',
zarobek money,

)

CREATE TABLE KlubZawodnika (
id_klub varchar(8) references Kluby(symbol),
id_zaw int references Zawodnicy(id_zaw), 
data_od date, 
data_do date,
CHECK (data_do > data_od)
)

ALTER TABLE Kluby ADD Sponsor varchar(20);
ALTER TABLE Kluby DROP CONSTRAINT UQ__Kluby__F072DFBE67926281;

ALTER TABLE KlubZawodnika DROP CONSTRAINT FK__KlubZawod__id_kl__173876EA; 

DROP TABLE Kluby;

insert into Zawodnicy
values( 'Fred', 20, 'Japan' , 1500);

insert into Zawodnicy
values( 'Bob', 18, 'England' , 1500);

insert into Zawodnicy
values( 'Stefix', 35, 'England' , 1500);

insert into Zawodnicy
values( 'Krem', 30, default,1500);

UPDATE Zawodnicy
SET zarobek = 1.1 * zarobek
WHERE kraj = 'Polska'

select * from Zawodnicy;