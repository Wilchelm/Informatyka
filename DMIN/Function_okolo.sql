
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
