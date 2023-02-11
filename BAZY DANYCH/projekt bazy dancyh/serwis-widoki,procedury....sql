create view v_pracownicy as 
select imie, nazwisko,stanowisko from Pracownicy;

create view v_klienci as
select imie, nazwisko from Klienci;

create view laptopy as
select * from Komputer where typ='laptop';

create view pc as
select * from Komputery where typ='pc';

﻿--wstawianie pracownika

create PROCEDURE wstawPracownika
	@Id_prac int,        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50),
	@Stanowisko varchar(30)
	AS
        if not exists (select * from Pracownik where imie=@Imie and nazwisko=@Nazwisko and mail=@Mail)
                insert into Pracownik values(@Id_prac, @Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail, @Stanowisko)
        else
                raiserror ('Jest juz taki pracownik', 11,1)

--sprawdzanie pracownika

create procedure sprawdzPracownika
        @Id_prac int,        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50),
	@Stanowisko varchar(30)
as
begin try
        exec wstawPracownika @Id_prac, @Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail, @Stanowisko
        print ' wstawilem wierszy: ' + cast(@@rowcount as varchar(10)) 
end try
begin catch
     print  'nie wstawilem wierszy, bo:  ' + cast(ERROR_NUMBER() as varchar(20)) + ' ' + ERROR_MESSAGE() 
end catch
print 'i dzialam dalej '



USUWANIE PROCEDURY: 		DROP PROC wstawPracownika
				DROP PROC sprawdzPracownika
	
WYWOŁANIE PROCEDURY:		sprawdzPracownika 6,'Anna', 'Kowalik','ul.Mostowa 9', '63-234 Płock', '516747895','kowalik@gmail.com', 'kierownik'

--usowanie pracownika

create PROCEDURE usunPracownika
        @nazwisko varchar(20)
AS
		if exists(select * from Pracownik where Nazwisko = @nazwisko)
			delete from Pracownik where Nazwisko=@nazwisko
        else
                raiserror ('nie ma takiego Pracownika', 11,1)

create procedure sprawdzUsuwaniePracownika
        @nazwisko varchar(20)
as
begin try
        exec usunPracownika @nazwisko
        print ' usunalem wierszy: ' + cast(@@rowcount as varchar(10)) 
end try
begin catch
     print  'nie usunale wierszy, bo:  ' + cast(ERROR_NUMBER() as varchar(20)) + ' ' + ERROR_MESSAGE() 
end catch
print 'i dzialam dalej '


DROP PROC SprawdzUsuwaniePracownika
DROP PROC usunPracownika

SprawdzUsuwaniePracownika 'Niewiadomska'

--wstawianie klienta

create PROCEDURE wstawKlienta
        @Id_kli int,        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50)
	AS
        if not exists (select * from Klient where Imie=@Imie and Nazwisko=@Nazwisko and telefon=@Telefon)
                insert into Klient values(@Id_kli, @Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail)
        else
                raiserror ('Jest juz taki klient', 11,1)

--sprawdzanie klienta

create procedure sprawdzKlienta
         @Id_kli int,        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50)
as
begin try
        exec wstawKlienta @Id_kli, @Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail
        print ' wstawilem wierszy: ' + cast(@@rowcount as varchar(10)) 
end try
begin catch
     print  'nie wstawilem wierszy, bo:  ' + cast(ERROR_NUMBER() as varchar(20)) + ' ' + ERROR_MESSAGE() 
end catch
print 'i dzialam dalej '




USUWANIE PROCEDURY: 		DROP PROC wstawKlienta
				DROP PROC sprawdzKlienta



WYWOŁANIE PROCEDURY:		sprawdzKlienta 'Adaml', 'Kasia', '999000777', 1, 0.4

--sprawdz nowe zgloszenie

create procedure wstaw_zgloszenie
	@ID int,
	@Kto int,
	@Naprawa varchar (30),
	@Stan varchar(30)
if not exists (select * from Zgloszenie where id=@ID)
	insert into Zgloszenie values(@ID, @Kto, @Naprawa, @Stan)
else
        raiserror ('Jest juz takie zlecenie', 11,1)

-- wyzwalacz zrealizowane zlecenie

create TRIGGER gotowe_do_odbioru
ON Zgloszenie
AFTER UPDATE
AS
	if update(aktualny_stan)
begin
 if exists(select * from Zgloszenie where aktualny_stan='gotowe do odbioru')
begin
RAISERROR ('Produkt gotowy do odbioru', 16, 1);
          ROLLBACK TRANSACTION;
       END
   END
GO

--zgloszenia do realizacji

create TRIGGER nowe_zlecenie
ON Zgloszenie
AFTER UPDATE
AS
	if update(aktualny_stan)
begin
 if exists(select * from Zgloszenie where aktualny_stan='przyjeto')
begin
RAISERROR ('Nowe zlecenie', 16, 1);
          ROLLBACK TRANSACTION;
       END
   END
GO
