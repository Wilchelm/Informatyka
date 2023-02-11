use serwis_komputerowy


go

CREATE VIEW v_pracownicy as 
select imie, nazwisko,stanowisko from Pracownicy

go

select * from v_pracownicy

go

create view v_klienci as
select imie, nazwisko from Klienci


go
 go
create view komputery as
select k.typ, p.nazwa as 'cpu', g.nazwa as 'gpu', g.pamiec, k.ram, d.typ as 'typ dysku', d.rozmiar as 'pojemnosc dysku', o.nazwa as 'os', k.wielkosc_matrycy, k.wartosc from Komputer k
inner join Procesor p on k.cpu=p.id_proc
inner join Grafika g on k.gpu=g.id_gpu
inner join Ram r on k.ram=r.id_ram
inner join Dysk d on k.rom=d.id_rom
inner join Os o on k.os= o.id_os
go

select * from komputery

go

create view zglosz as
select z.kto, p.imie as 'Imie pracownika', p.nazwisko as 'Nazwisko pracownika', k.imie, k.nazwisko, s.nazwa as 'Status'  from Zgloszenie z
inner join Pracownicy p on z.kto=p.id_prac
inner join Klienci k on z.kto_naprawia=k.id_kli
inner join Statusy s on z.aktualny_stan=s.id_stat

select* from zglosz

go

select * from zglosz

drop view laptopy

go

select * from laptopy


go

go
create view gotowe as
select * from Zgloszenie where aktualny_stan='gotowe do odbioru'

go
go
create view nowe as
select* from Zgloszenie where aktualny_stan='przyjeto'

go

﻿--wstawianie pracownika
go
create PROCEDURE wstawPracownika        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50),
	@Stanowisko varchar(30)
	AS
        if not exists (select * from Pracownicy where imie=@Imie and nazwisko=@Nazwisko and mail=@Mail)
                insert into Pracownicy values(@Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail, @Stanowisko)
        else
                raiserror ('Jest juz taki pracownik', 11,1)

go

--sprawdzanie pracownika

create procedure sprawdzPracownika        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50),
	@Stanowisko varchar(30)
as
begin try
        exec wstawPracownika @Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail, @Stanowisko
        print ' wstawilem wierszy: ' + cast(@@rowcount as varchar(10)) 
end try
begin catch
     print  'nie wstawilem wierszy, bo:  ' + cast(ERROR_NUMBER() as varchar(20)) + ' ' + ERROR_MESSAGE() 
end catch
print 'i dzialam dalej '

go



--USUWANIE PROCEDURY: 		DROP PROC wstawPracownika
				--DROP PROC sprawdzPracownika
	
--WYWOŁANIE PROCEDURY:		sprawdzPracownika 'Anna', 'Kowalik','ul.Mostowa 9', '63-234 Płock', '516747895','kowalik@gmail.com', 'kierownik'
select * from Pracownicy
--usowanie pracownika
go
create PROCEDURE usunPracownika
        @nazwisko varchar(20)
AS
		if exists(select * from Pracownicy where nazwisko = @nazwisko)
			delete from Pracownicy where nazwisko=@nazwisko
        else
                raiserror ('nie ma takiego Pracownika', 11,1)
go
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
go
SprawdzUsuwaniePracownika 'Niewiadomska'

select * from Pracownicy

--wstawianie klienta
go
create PROCEDURE wstawKlienta        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50)
	AS
        if not exists (select * from Klienci where Imie=@Imie and Nazwisko=@Nazwisko and telefon=@Telefon)
                insert into Klienci values(@Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail)
        else
                raiserror ('Jest juz taki klient', 11,1)

--sprawdzanie klienta
go
create procedure sprawdzKlienta        
	@Imie varchar(20),
	@Nazwisko varchar(20),
	@Adres varchar(30),
	@Miasto varchar(30),
	@Telefon varchar(9),
	@Mail varchar(50)
as
begin try
        exec wstawKlienta @Imie, @Nazwisko, @Adres, @Miasto, @Telefon, @Mail
        print ' wstawilem wierszy: ' + cast(@@rowcount as varchar(10)) 
end try
begin catch
     print  'nie wstawilem wierszy, bo:  ' + cast(ERROR_NUMBER() as varchar(20)) + ' ' + ERROR_MESSAGE() 
end catch
print 'i dzialam dalej '




--USUWANIE PROCEDURY: 		DROP PROC wstawKlienta
				--DROP PROC sprawdzKlienta



--WYWOŁANIE PROCEDURY:		sprawdzKlienta 'Al', 'Takt', 'ul.Nowej Ziemi 38', '24-515 Warszawa','758930287','takt@gmail.com'

--sprawdz nowe zgloszenie
go
create procedure wstaw_zgloszenie
	@Kto int,
	@Kto_nap int,
	@Naprawa varchar (30),
	@Stan int
	as
	begin
if not exists (select * from Zgloszenie where id=@ID)
	insert into Zgloszenie values(@Kto,@Kto_nap , @Naprawa, @Stan)
else
        raiserror ('Jest juz takie zlecenie', 11,1)
	end

	--wywolanie wstaw_zgloszenie 4,3,'instalacja systemu','1'

select* from Zgloszenie

-- wyzwalacz zrealizowane zlecenie
go
create TRIGGER gotowe_do_odbioru
ON Zgloszenie
AFTER UPDATE
AS
	if update(aktualny_stan)
begin
 if exists(select * from Zgloszenie where aktualny_stan='gotowe do odbioru')
begin
select * from gotowe
       END
   END
GO

select * from Zgloszenie
--drop trigger gotowe_do_odbioru
go
create TRIGGER nowe_zlec
ON Zgloszenie
AFTER UPDATE
AS
	if update(aktualny_stan)
begin
 if exists(select * from Zgloszenie where aktualny_stan='przyjeto')
begin
select * from nowe
       END
   END
GO

drop trigger nowe_zlec

update Zgloszenie set aktualny_stan ='przyjeto' where id=2
go
create trigger blok_prac
on Pracownicy
after update
as
if update(imie) or update(nazwisko)
begin
raiserror ('nie mozna zmienic imion, nazwisk pracownikow', 11,1)
rollback transaction
end

drop trigger blok_prac

update Pracownicy set imie = 'Adam' where id_prac = 1
go
create trigger blok_kli
on Klienci
after update
as
if update(imie) or update(nazwisko)
begin
raiserror ('nie mozna zmienic imion, nazwisk klientow', 11,1)
rollback transaction
end

drop trigger blok_kli

update Klienci set imie = 'Adam' where id_kli = 1





--raport ile jaki klient kupil
go
create procedure ile @klient int
as
	if exists(select * from Zgloszenie where kto=@klient)
begin (select count(*) from Zgloszenie where kto=@klient)
end
else
begin select 'Nie ma takiego klienta'
end
select * from Zgloszenie

ile 5

















