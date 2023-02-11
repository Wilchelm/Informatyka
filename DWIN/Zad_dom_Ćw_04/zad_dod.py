x=input() #wczytujemy ciag znaków
licz_zera=0 #ustawiamy zmienne pomocnicze
licz_jedynki=0
pom=2
for i in x: #czytamy znaki
  if i=="0" and pom==1: #sprawdzamy jaki to znak i czy znak się nie zmienił
#jeśli znak się zmienił to wypisujemy znak oraz liczbe jego wystąpień i zerujemy zmienne pomocnicze
    pom=2
    print ("1[",licz_jedynki,"]",sep="")
    licz_zera=0
    licz_jedynki=0  
  if i=="1" and pom==0: #podobnie jak wyżej
    pom=2
    print ("0[",licz_zera,"]",sep="")
    licz_zera=0
    licz_jedynki=0
  if i=="0" and pom!=1: #sprawdzamy znak i zwiekszamy liczbe jego wystąpienia
    pom=0
    licz_zera+=1
  if i=="1" and pom!=0: #podobnie jak wyżej
    pom=1
    licz_jedynki+=1

#dlatego, że w pętli wypisuję tylo po zmianie znaku z 1 na 0 i odwrotnie 
#to muszę wypisać ostatni znak i jego liczbe powtórzeń
if pom==1:
  print ("1[",licz_jedynki,"]",sep="") 
if pom==0:
  print ("0[",licz_zera,"]",sep="")
