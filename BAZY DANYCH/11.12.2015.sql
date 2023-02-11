
create database zadania11_12

-----------------------------------------
-- Tworzenie tabel --
-----------------------------------------
create table gatunki
(id_gatunek int primary key,
 nazwa varchar(30),
 kontynent varchar(10),
 rodzaj varchar(15));

create table zwierzaki
(id_gatunek int references gatunki(id_gatunek),
 nazwa varchar(50),
 waga float,
 rok_ur int,
 typ varchar(30));

 -----------------------------------------
-- Wypelnianie tabel danymi--
-----------------------------------------
insert into gatunki
values(1, 'Lew', 'Afryka','Ladowe');
insert into gatunki
values(2, 'Tygrys', 'Azja','Ladowe');
insert into gatunki
values(3, 'Foka Wielka', 'Austaralia','Wodne');
insert into gatunki
values(4, 'Mucha Tse-tse' ,'Afryka','Latajace');
insert into gatunki
values(5, 'Tygrys', 'Afryka','Ladowe');
insert into gatunki
values(6, 'Bocian' ,'Europa','Latajace');
insert into gatunki
values(7, 'Panda Wielka' ,'Azja','Ladowe');
insert into gatunki
values(8, 'Golab' ,'Azja','Latajace');
insert into gatunki
values(9, 'Golab' ,'Europa','Latajace');
insert into gatunki
values(10, 'Zyrafa' ,'Afryka','Ladowe');

insert into zwierzaki
values(1, 'Simba', 120, 2001, 'drapiezny');
insert into zwierzaki
values(4, 'Dzika Mea', 0.05, 2008, 'uciazliwy');
insert into zwierzaki
values(4, 'Fly Rock', 0.05, 2008, 'uciazliwy');
insert into zwierzaki
values(2, 'Tygrysek', 100, 2006, 'drapiezny');
insert into zwierzaki
values(6, 'Bociek', 25, 2002, 'lagodny');
insert into zwierzaki
values(6, 'Kle Kle', 30, 2003, 'lagodny');
insert into zwierzaki
values(5, 'Wild Leo', 140, 2000, 'drapiezny');
insert into zwierzaki
values(7, 'Pao', 90, 2004, 'lagodny');
insert into zwierzaki
values(8, 'Flyek', 2, 2005, 'udomowiony');
insert into zwierzaki
values(9, 'PostMan', 2, 2004, 'udomowiony');
insert into zwierzaki
values(8, 'Bobek', 2, 2006, 'udomowiony');
insert into zwierzaki
values(10, 'Dluga Ula', 100, 2006, 'udomowiony');
insert into zwierzaki
values(10, 'Linea', 112, 2005, 'udomowiony');
insert into zwierzaki
values(10, 'Mikki', 134, 2004, 'udomowiony');


--zadanie 1--
select *  from gatunki where kontynent = 'Azja'
order by nazwa
--zad 2--
select * from gatunki where nazwa > some(select nazwa from zwierzaki where typ= 'drapiezny');
--zad 3--
select * from zwierzaki where rok_ur>2004 AND SUM(id_)>2;
--zad 4
select nazwa from gatunki where nazwa like '%Wielka%';
--zad 5
select top 1 nazwa, MIN(waga) from zwierzaki where typ='udomowiony' group by nazwa;
--zad 6
select avg(waga) from zwierzaki z join gatunki g on z.id_gatunek = g.id_gatunek where g.nazwa='Zyrafa'
--zad 7
select typ , 2015-min(rok_ur) as'wiek'  from zwierzaki group by typ;
--zad 8
select typ, count(typ) from zwierzaki group by typ;
--zad 9
select typ from zwierzaki group by typ having count(*)>3; 
--zad 10 
select kontynent, count(kontynent) from gatunki group by kontynent
inner join gatunki g
on z.id_gatunek = g.id_gatunek;
