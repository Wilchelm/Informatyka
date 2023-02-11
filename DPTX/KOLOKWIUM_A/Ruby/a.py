#!/usr/bin/python3

import re
import sys

usunieto=0

x1=sys.stdin.read()
x=re.findall(".*#",x1)
y = re.findall("[0-9]+", x[0])
if (len(y)>0):
    suma = 0
    for i in y:
        suma = suma+int(i)
    if suma>100:
        print (x)
    else:
        usunieto=usunieto+1

print ("USUNIĘTO:",usunieto)
            

    
   

