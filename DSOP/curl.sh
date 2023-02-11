#!/bin/bash
for i in {001..100}
do
  k=$(curl -s "https://bap.faculty.wmi.amu.edu.pl/_f/suma/"$i".txt")
  wynik=$((wynik+k))
done
echo $wynik
 	
