use zadanie1

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

 


select * from Dzialy WHERE id_dzialu=20;

SELECT adres from Dzialy;

SELECT DISTINCT adres from Dzialy;

SELECT * FROM Pracownicy WHERE szef=130 AND (placa_dod+placa_pod)>1500;

SELECT nazwa FROM Stanowiska WHERE (1300<placa_max AND placa_max<=1600) OR (1300<placa_min AND placa_min<1600);

SELECT COUNT(id_dzialu) AS 'Liczba dzialo' From Dzialy;

SELECT AVG(placa_pod), MIN(placa_dod) AS 'Srednia placa podst.' FROM Pracownicy;

SELECT nazwa, SUM(placa_min) FROM Stanowiska GROUP BY nazwa;

SELECT nazwa, SUM(placa_min) FROM Stanowiska GROUP BY nazwa HAVING AVG(placa_min)>1500;

SELECT nazwisko FROM Pracownicy WHERE nazwisko LIKE 'K%';

SELECT TOP 1 nazwisko FROM Pracownicy ORDER BY placa_dod+placa_pod DESC;

SELECT nazwisko FROM Pracownicy WHERE nazwisko LIKE '%rz%' ;

SELECT nazwisko FROM Pracownicy WHERE nazwisko LIKE '[^a-d]%' ;

SELECT TOP 3 nazwa FROM Stanowiska ORDER BY placa_min DESC;
