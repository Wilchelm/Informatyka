# -*- coding: utf-8 -*-
import os, re

command = 'echo "Na ulicy stał żółty samochód, czerwony motocykl i zielony rower." | sudo docker run -i skorzewski/psi-toolkit lemmatize --lang pl ! puddle > D01.txt'
wynik = []
os.system(command)
my_dir = os.path.expanduser('D01.txt')
f = open(my_dir , 'r')
while f.readline():
	line = f.readline()
	wynik += re.findall(r'([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._]+)[ ]*!pl,parse,puddle[ ]*NP,case=', line)
print (wynik)
