
-----1-------

select SUM(Brutto) from Wynagrodzenie
where ID_Oddzialu in
	(select ID_Oddzialu from Oddzialy where Skrot = 'ODDZ IOM')
	and ID_Czasy = 701


----2------

select COUNT(distinct ID_Pracownika) from Zatrudnienia
where  RokZatrudnienia < 2001 and RokZwolnienia = 0

----3-----

select SUM(DniChor) from Wynagrodzenie
where ID_GrupyZawodowej in
	(select ID_GrupyZawodowej from GrupyZawodowe where Nazwa_GrupyZawodowej = 'PIELÊGNIARKI')

----4------
select Stanowisko from Zatrudnienia
GROUP BY Stanowisko
HAVING ( COUNT(Stanowisko) > 1 )

select AVG(Brutto) from Wynagrodzenie w  join Zatrudnienia z
on w.ID_Czasy = z.ID_Czasy
WHERE (Stanowisko = 'M£ODSZY ASYSTENT' OR Stanowisko = 'M£.AS.PIEL.EPI' OR Stanowisko= 'M£.ASYST.REZ.') AND w.ID_Czasy = '701'


----------

select count(*) from Wynagrodzenie
group by ID_Pracownika, ID_Czasy, ID_GrupyZawodowej, ID_Oddzialu
having count(*) >1

select * from Zatrudnienia