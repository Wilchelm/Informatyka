#!/usr/bin/python3

import re, urllib

urllib.urlretrieve("http://sp118.pl/pl/lista_adresow_email_do_nauczycieli,36.html", "test.txt")

f=open("test.txt", "r")
text = f.read()
f.close()

m = re.findall(r"([a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)",text)
print m
