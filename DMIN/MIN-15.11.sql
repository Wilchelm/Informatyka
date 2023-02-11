Create database MIN_DW
go

use MIN_DW
go

create table Filmy
(id int identity(1,1) primary key,
tytul varchar(100) not null,
rezyser varchar(100) not null,
kraj varchar(50),
rok_produkcji int,
budzet money,
czas int,
gatunek varchar(50));


insert into Filmy
values ('Odlot', 'Peter Docter, Bob Peterson', 'USA', 2009, 175000000, 96, 'animacja');

insert into Filmy
values ('Bêkarty wojny', 'Quentin Tarantino', 'USA/Niemcy', 2009, 70000000, 153, 'akcja' );

insert into Filmy
values ('Gdzie Jest Nemo?', 'Andrew Stanton , Lee Unkrich', 'USA', 2003, 94000000, 100, 'animacja' );

insert into Filmy
values ('Prosta historia', 'David Lynch', 'USA', 1999, 10000000, 112, 'obyczajowy');

insert into Filmy
values ('¯ycie jest piêkne', 'Roberto Benigni', 'W³ochy', 1997, 57000000, 116, 'dramat, komedia');

insert into Filmy
values ('Kill Bill','Quentin Tarantino', 'USA', 2003, 41000000, 111, 'akcja' );

insert into Filmy
values ('Ch³opaki nie p³acz¹', 'Olaf Lubaszenko', 'Polska', 2000, null, 100, 'komedia sensacyjna');


select * from Filmy
order by budzet



/*****************************************************************

Na potrzeby zamodelowania zbioru rozmytego:

wzor na prosta przechodzaca przez dwa punkty (xa, ya) i (xb, yb):

y - ya = (yb - ya)/(xb-xa) * (x-xa)

******************************************************************/

-------------------------------------------------------------------
-------- Nieprecyzyjne zapytania do bazy danych        ------------
-------------------------------------------------------------------

-- REALIZAJA WARUNKÓW NIEPRECYZYJNYCH

-------- 1. Tworzenie zmiennej lingwistycznej

--drop table zmienne_lingwistyczne

create procedure dodaj_term(@nazwa_zmiennej varchar(100), @term varchar(100), @a int, @b int, @c int)
as
begin
	-- jesli tabela zmienne_lingwistyczne nie istnieje to ja utworz 
	IF  OBJECT_ID ('zmienne_lingwistyczne') IS NULL
		create table zmienne_lingwistyczne
		(nazwa_zmiennej varchar(100),
		term varchar(100),
		a int,
		b int,
		c int,
		check(b>=a),
		check(c>=b))
	-- wstaw nowy term interpretowany za pomoca funkcji trojkatnej
	insert into zmienne_lingwistyczne
	values (@nazwa_zmiennej, @term, @a, @b, @c)
end
go

-- wywolanie procedury (przyk³ad)

exec dodaj_term 'budzet', 'niski', 0,0, 50000000
exec dodaj_term 'budzet', 'sredni', 0, 50000000, 100000000
exec dodaj_term 'budzet', 'wysoki', 50000000, 100000000, 100000000

-- w analogiczny sposob dodaj zmienna lingwistyczna "rok produkcji"


--------- 2. Funkcja 'fuzyfikuj¹ca' - szkielet
drop function dbo.fuzzy

create function dbo.fuzzy(@x real, @nazwa varchar(100),@term varchar(100))
returns real
as
begin
declare @membership real

select @membership = case
	when a=b and b<c and @x <= b then 1.0
	when a=b and b<c and @x>b and @x<c then (c-@x)/(c-b)
	when a=b and b<c and @x>c then 0.0
	when a<b and c>b and (@x<=a or @x>=c) then 0.0
	when a<b and c>b and @x<b then (@x-a)/(b-a)
	when a<b and c>b and @x<c then (c-@x)/(c-b)
	when a<b and b=c and @x<=a then 0.0
	when a<b and b=c and @x<=a then 0.0
	when a<b and b=c and @x<b then (@x-a)/(b-a)
	when a<b and b=c and @x>=b then 1.0
	else 0.0
	end
from zmienne_lingwistyczne
where nazwa_zmiennej = @nazwa
and term = @term

return @membership
end

go

---------- 3. Realizacja zapytania nieprecyzyjnego

-- 1. Podaj tytu³y filmów niskobud¿etowych.

select *, dbo.fuzzy(budzet,'budzet', 'niski') as stopien_przynaleznosci
from filmy
where dbo.fuzzy(budzet,'budzet', 'niski') >0
order by stopien_przynaleznosci DESC;

-- 2. Podaj informacje o filmach nowych.
select * from Filmy 



--------------------
exec dodaj_term 'czas', 'okolo 100min', 80,100,120

select *, dbo.fuzzy(czas, 'czas' , 'okolo 100min') as stopien_przynaleznosci
from filmy
where dbo.fuzzy(czas, 'czas' , 'okolo 100min') >0
order by stopien_przynaleznosci DESC;

exec dodaj_term 'rok_produkcji', 'okolo 2000' , 1995, 2000, 2005, 2010

select *, dbo.fuzzy(rok_produkcji, 'rok_produkcji', 'okolo 2000') as stopien_przynaleznosci
from filmy
where dbo.fuzzy(rok_produkcji, 'rok_produkcji', 'okolo 2000') >0
order by stopien_przynaleznosci DESC;


-------OKOLO-------
------___/\___-----

drop function okolo
go
create function dbo.okolo(@x real, @wart real)
returns real
as
begin
declare @membership real

if @wart > 1000 
select @membership = case
	when @x = @wart then 1.0
	when @x > @wart and @x < (@wart*1.005) then  ((@wart*1.005)-@x) / ((@wart*1.005)-@wart)
	when @x < @wart and @x > (@wart*0.995) then (@x-(@wart*0.995)) / (@wart - (@wart*0.995)) 
	else 0.0
	end
else 
select @membership = case
	when @x = @wart then 1.0
	when @x > @wart and @x < (@wart*1.1) then  ((@wart*1.1)-@x) / ((@wart*1.1)-@wart)
	when @x < @wart and @x > (@wart*0.9) then (@x-(@wart*0.9)) / (@wart - (@wart*0.9)) 
	else 0.0
	end
return @membership
end


go
----------1----------
select *, dbo.okolo(czas,100) as stopien_przynaleznosci
from filmy
where dbo.okolo(czas,100) >0
order by stopien_przynaleznosci DESC;
go
----------2----------
select *, dbo.okolo(rok_produkcji,2000)  as stopien_przynaleznosci
from filmy
where dbo.okolo(rok_produkcji,2000) >0
order by stopien_przynaleznosci DESC;
go
