#!/usr/bin/python3
import re

name = raw_input("Podaj imie ")

if re.search(r"[A-Z][a-zA-Z]+",name)is None:
	print "To nie jest imie"

surname = raw_input("Podaj nazwisko ")

if re.search(r"[A-Z][a-zA-Z]+",surname)is None:
	print "To nie jest nazwisko"

city = raw_input("Podaj miasto ")

if re.search(r"[A-Z][a-zA-Z]+",city)is None:
	print "To nie jest miasto"

phone = raw_input("Podaj numer ")

if re.search(r"\(\d\d\) \d{3}\-\d{2}\-\d{2}",phone)is None:
	print "To nie jest numer telefonu"

post_code = raw_input("Podaj kod pocztowy ")

if re.search(r"\d{2}\-\d{3}",post_code)is None:
	print "To nie jest kod pocztowy"

