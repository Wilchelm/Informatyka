create database zadania18_12_2015


GO

SET LANGUAGE polski
GO

--------- CREATE

create table Stanowiska
(nazwa varchar(10) primary key,
placa_min money,
placa_max money,
check (placa_min<placa_max));


create table Pracownicy
(id int not null primary key,
nazwisko varchar(20) not null,
szef int references Pracownicy(id),
placa money,
stanowisko varchar(10) references Stanowiska(nazwa),
zatrudniony date);

create table Projekty
(id int identity(10,10) not null primary key,
nazwa varchar(20) not null unique,
dataRozp datetime not null,
dataZakonczPlan datetime not null,
dataZakonczFakt datetime null,
kierownik int references Pracownicy(id),
stawka money);

create table Realizacje
(idProj int references Projekty(id),
idPrac int references Pracownicy(id),
godzin real default 8);

GO

---------- INSERT


insert into Stanowiska
values ('profesor', 3000, 5000);
insert into Stanowiska
values ('adiunkt', 2000, 3000);
insert into Stanowiska
values ('doktorant', 900, 1300);
insert into Stanowiska
values ('sekretarka', 1500, 2500);
insert into Stanowiska
values ('techniczny', 1500, 2500);



insert into Pracownicy
values(1, 'Wachowiak', null, 4500, 'profesor', '01-09-1980');
insert into Pracownicy
values(2, 'Jankowski', 1, 2500, 'adiunkt', '01-09-1990');
insert into Pracownicy
values(3, 'Fio³kowska', 1, 2550, 'adiunkt', '01-01-1985');
insert into Pracownicy
values(4, 'Mielcarz', 1, 4000, 'profesor', '01-12-1980');
insert into Pracownicy
values(5, 'Ró¿ycka', 4, 2800, 'profesor', '01-09-2001');
insert into Pracownicy
values(6, 'Miko³ajski', 4, 1000, 'doktorant', '01-10-2002');
insert into Pracownicy
values(7, 'Wójcicki', 5, 1350, 'doktorant', '01-10-2003');
insert into Pracownicy
values(8, 'Listkiewicz', 1, 2200, 'sekretarka', '01-09-1980');
insert into Pracownicy
values(9, 'Wróbel', 1, 1900, 'techniczny', '01-01-1999');
insert into Pracownicy
values(10, 'Andrzejewicz', 5, 2900, 'adiunkt', '01-01-2002');


insert into Projekty
values('e-learning','01-01-2009', '31-05-2010', null, 5, 100);
insert into Projekty
values('web service', '10-11-1999', '31-12-2000', '20-04-2001', 4, 90)
insert into Projekty
values('semantic web', '01-10-2007', '01-09-2009', null, 4, 85)
insert into Projekty
values('neural network', '01-01-1998', '30-06-2000', '30-06-2000', 1, 120)


insert into Realizacje
values(10, 5, 8)
insert into Realizacje
values(10, 10, 6)
insert into Realizacje
values(10, 9, 2)

insert into Realizacje
values(20, 4, 8)
insert into Realizacje
values(20, 6, 8)
insert into Realizacje
values(20, 9, 2)

insert into Realizacje
values(30, 4, 8)
insert into Realizacje
values(30, 6, 6)
insert into Realizacje
values(30, 10, 6)
insert into Realizacje
values(30, 9, 2)

insert into Realizacje
values(40, 1, 8)
insert into Realizacje
values(40, 2, 4)
insert into Realizacje
values(40, 3, 4)
insert into Realizacje
values(40, 9, 2)



------------ SELECT

select * from Stanowiska
select * from Pracownicy
select * from Projekty
select * from Realizacje




-- Procedury przyklad--

CREATE PROCEDURE KIEROWNIK
        @NR_PROJ INT,
        @NAZWISKO VARCHAR(20) OUTPUT
AS
BEGIN TRY
        IF EXISTS (SELECT * FROM PROJEKTY WHERE ID=@NR_PROJ)
        BEGIN
                SELECT @NAZWISKO = NAZWISKO
                FROM PRACOWNICY
                WHERE ID = (SELECT KIEROWNIK FROM PROJEKTY WHERE  ID = @NR_PROJ)
        END
        ELSE
                RAISERROR ('NIE MA TAKIEGO PROJEKTU', 11,1)
END TRY
BEGIN CATCH
                SELECT ERROR_NUMBER() AS 'NUMER BLEDU',ERROR_MESSAGE() AS 'KOMUNIKAT'
END CATCH
--test przykladu--
DECLARE @NAZW VARCHAR(20)
EXEC KIEROWNIK 100, @NAZW OUTPUT
PRINT @NAZW

--zad 1
CREATE PROCEDURE Zatrudnij_Pracownika
@ID_PRAC INT OUTPUT
AS
BEGIN 
SELECT id FROM Pracownicy
WHERE zatrudniony=(SELECT MAX(zatrudniony) FROM Pracownicy)
END
--Wywolanie
DECLARE @ID_PRAC INT
EXEC Zatrudnij_Pracownika @ID_PRAC OUTPUT
PRINT @ID_PRAC
--ZADANIE 2
CREATE PROCEDURE pracownik_to_projekt
@ID_PRACOWNIKA INT,
@ID_PROJEKTU INT,
@GODZ datetime 
AS
BEGIN TRY
IF  @GODZ >=8 Begin
	IF EXISTS (SELECT * FROM Pracownicy WHERE id is not null)BEGIN
	 	IF EXISTS (SELECT * FROM Projekty WHERE id is not null) BEGIN
			IF EXISTS(SELECT * FROM Projekty WHERE dataZakonczFakt is not null)
			BEGIN
			INSERT INTO Realizacje VALUES (@ID_PROJEKTU, @ID_PRACOWNIKA, @GODZ)
			ELSE
			RAISERROR ('PROJEKT NIE ZAKONCZONY')
		ELSE
		RAISERROR ('NIE MA PROJEKTU')
	ELSE
	RAISERROR ('NIE MA PRACOWNIKA')	END
ELSE
RAISERROR ('ZADUZO GODZIN')
END TRY
BEGIN CATCH
                SELECT ERROR_NUMBER() AS 'NUMER BLEDU',ERROR_MESSAGE() AS 'KOMUNIKAT'
END CATCH