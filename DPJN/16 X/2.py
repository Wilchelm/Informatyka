#!/usr/bin/python3

import re

f=open("2.csv", "r")
for line in f:
	if re.search(r".*\;\d+\;\d+",line):
		print "Ok "
	else: 
		print "Niepoprawny "
	
