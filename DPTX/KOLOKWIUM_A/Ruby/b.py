#!/usr/bin/python3

import re
import sys

def unique(list1): 
      
    # insert the list to the set 
    list_set = set(list1) 
    # convert the set to the list 
    unique_list = list(list_set)
    return unique_list

usunieto=0
l = []
l2 = []
for line in sys.stdin:
    x = re.findall("([a-z]+)[ \t]*=[ \t]*([0-9]+)", line)
    l.append((x[0][0],x[0][1]))
    l2.append(x[0][0])

l2 = unique(l2)
l3 = []
for i in l2:
    suma = 0
    for i2 in l:
        if i == i2[0]:
            suma = suma + int(i2[1])
    l3.append(i+"="+str(suma))
for i in sorted(l3):
    print(i)
