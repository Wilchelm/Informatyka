#!/usr/bin/python3

a = float(raw_input("Podaj a "))
b = float(raw_input("Podaj b "))
c = float(raw_input("Podaj c "))
x1 = float(raw_input("Podaj x1 "))
x2 = float(raw_input("Podaj x2 "))
x3 = float(raw_input("Podaj x3 "))
x4 = float(raw_input("Podaj x4 "))
x5 = float(raw_input("Podaj x5 "))


def licz(x,a,b,c):
	if a==b and b<c and x<=b:
		wynik=1
	elif a==b and b<c and x>b and x<c:
		wynik=(c-x)/(c-b)
	elif a==b and b<c and x>c:
		wynik=0
	elif a<b and c>b and (x<=a or x>=c):
		wynik=0
	elif a<b and c>b and x<b:
		wynik=(b-x)/(b-a)
	elif a<b and c>b and x<c:
		wynik=(c-x)/(c-b)
	elif a<b and b==c and x<=a:
		wynik=0 
	elif a<b and b==c and x<b:
		wynik=(b-x)/(b-a)
	elif a<b and b==c and x>=b:
		wynik=1
	else:
		wynik=0
	return wynik


print "f(x1) =", licz(x1,a,b,c)
print "f(x2) =", licz(x2,a,b,c)
print "f(x3) =", licz(x3,a,b,c)
print "f(x4) =", licz(x4,a,b,c)
print "f(x5) =", licz(x5,a,b,c)


