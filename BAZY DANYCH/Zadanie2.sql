create database zadanie2
use zadanie2

CREATE TABLE Dzialy(
    id_dzialu INT NOT NULL PRIMARY KEY,
    nazwa     VARCHAR(30) NOT NULL,
    adres     VARCHAR(30) NOT NULL
);

CREATE TABLE Stanowiska(
    nazwa     VARCHAR(30) NOT NULL PRIMARY KEY,
    placa_min MONEY,
    placa_max MONEY,
    CHECK (placa_min <= placa_max)
);


CREATE TABLE Pracownicy(
    id_prac     INT NOT NULL PRIMARY KEY,
    nazwisko    VARCHAR(30),
    stanowisko  VARCHAR(30) REFERENCES Stanowiska(nazwa),
    szef        INT REFERENCES Pracownicy(id_prac),
    zatrudniony DATETIME,
    placa_pod   MONEY,
    placa_dod   MONEY,
    id_dzialu   INT REFERENCES Dzialy(id_dzialu)
);

INSERT INTO Dzialy VALUES (10,'ADMINISTRACJA',      'PIOTROWO 3A');
INSERT INTO Dzialy VALUES (20,'SYSTEMY ROZPROSZONE','PIOTROWO 3A');
INSERT INTO Dzialy VALUES (30,'SYSTEMY EKSPERCKIE', 'STRZELECKA 14');
INSERT INTO Dzialy VALUES (40,'ALGORYTMY',          'WLODKOWICA 16');
INSERT INTO Dzialy VALUES (50,'BADANIA OPERACYJNE', 'MIELZYNSKIEGO 30');

INSERT INTO Stanowiska VALUES ('PROFESOR'  ,1800.00, 2500.00);
INSERT INTO Stanowiska VALUES ('ADIUNKT'   ,1510.00, 1750.00);
INSERT INTO Stanowiska VALUES ('ASYSTENT'  ,1300.00, 1500.00);
INSERT INTO Stanowiska VALUES ('STAZYSTA'  ,1150.00, 1250.00);
INSERT INTO Stanowiska VALUES ('SEKRETARKA',1270.00, 1450.00);
INSERT INTO Stanowiska VALUES ('DYREKTOR'  ,2280.00, 3100.00);
 
INSERT INTO Pracownicy VALUES (100,'WEGLARZ'    ,'DYREKTOR'  ,NULL, '01-JAN-68', 2730.00, 420.50,10);
INSERT INTO Pracownicy VALUES (110,'BLAZEWICZ'  ,'PROFESOR'  ,100 , '01-MAY-73', 2350.00, 210.00,40);
INSERT INTO Pracownicy VALUES (120,'SLOWINSKI'  ,'PROFESOR'  ,100 , '01-SEP-77', 2070.00,   NULL,30);
INSERT INTO Pracownicy VALUES (130,'BRZEZINSKI' ,'PROFESOR'  ,100 , '01-JUL-68', 1960.00,   NULL,20);
INSERT INTO Pracownicy VALUES (140,'MORZY'      ,'PROFESOR'  ,130 , '15-SEP-75', 1830.00, 105.00,20);
INSERT INTO Pracownicy VALUES (150,'KROLIKOWSKI','ADIUNKT'   ,130 , '01-SEP-77', 1645.50,   NULL,20);
INSERT INTO Pracownicy VALUES (160,'KOSZLAJDA'  ,'ADIUNKT'   ,130 , '01-MAR-85', 1590.00,   NULL,20);
INSERT INTO Pracownicy VALUES (170,'JEZIERSKI'  ,'ASYSTENT'  ,130 , '01-OCT-92', 1439.50,  80.50,20);
INSERT INTO Pracownicy VALUES (190,'MATYSIAK'   ,'ASYSTENT'  ,140 , '01-SEP-93', 1371.00,   NULL,20);
INSERT INTO Pracownicy VALUES (180,'MAREK'      ,'SEKRETARKA',100 , '20-FEB-85', 1410.50,   NULL,10);
INSERT INTO Pracownicy VALUES (200,'ZAKRZEWICZ' ,'STAZYSTA'  ,140 , '15-JUL-94', 1260.00,   NULL,30);
INSERT INTO Pracownicy VALUES (210,'BIALY'      ,'STAZYSTA'  ,130 , '15-OCT-93', 1250.00, 170.50,30);
INSERT INTO Pracownicy VALUES (220,'KONOPKA'    ,'ASYSTENT'  ,110 , '01-OCT-93', 1480.00,   NULL,20);
INSERT INTO Pracownicy VALUES (230,'HAPKE'      ,'ASYSTENT'  ,120 , '01-SEP-92', 1480.00,  90.00,30);
 
/*zadanie1*/
SELECT p.id_prac, p.nazwisko, d.nazwa 
FROM Pracownicy p JOIN Dzialy d
on p.id_dzialu=d.id_dzialu
/*zadanie2*/
SELECT p.nazwisko, p.stanowisko, s.placa_min, s.placa_max
From Pracownicy p JOIN Stanowiska s
on p.stanowisko=s.nazwa
/*zadanie3*/
SELECT p.nazwisko, p.id_prac, p.stanowisko, d.nazwa, s.placa_min, s.placa_max
From Pracownicy p
JOIN Stanowiska s
on p.stanowisko=s.nazwa
Join Dzialy d
on p.id_dzialu=d.id_dzialu 
/*zadanie4*/
SELECT szef, count(*)FROM Pracownicy GROUP BY szef;
/*zadanie5*/
SELECT stanowisko, count(placa_pod) FROM Pracownicy 
GROUP BY stanowisko HAVING count(placa_pod)>3
--Zadanie 6
SELECT nazwa, AVG(placa_pod+isnull(placa_dod,0)) FROM Pracownicy join Dzialy on stanowisko='ASYSTENT' AND placa_pod+placa_dod<2000 group by nazwa
--zadanie 7
SELECT nazwisko FROM Pracownicy JOIN Dzialy on adres='PIOTROWO 3A'