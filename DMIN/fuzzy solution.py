#!/usr/bin/python3


i = int(raw_input("1-funkcja przynaleznosci\n2-przekroj zbiorow\n3-suma zbiorow\n4-dopelnienie zbioru\n"))

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
			wynik=(x-a)/(b-a)
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

if i==1:
	a = float(raw_input("Podaj a "))
	b = float(raw_input("Podaj b "))
	c = float(raw_input("Podaj c "))
	x1 = float(raw_input("Podaj x1 "))
	x2 = float(raw_input("Podaj x2 "))
	x3 = float(raw_input("Podaj x3 "))
	x4 = float(raw_input("Podaj x4 "))
	x5 = float(raw_input("Podaj x5 "))

	print "f(x1) =", licz(x1,a,b,c)
	print "f(x2) =", licz(x2,a,b,c)
	print "f(x3) =", licz(x3,a,b,c)
	print "f(x4) =", licz(x4,a,b,c)
	print "f(x5) =", licz(x5,a,b,c)
elif i==2:
	a = float(raw_input("Podaj a zbioru A "))
	b = float(raw_input("Podaj b zbioru A "))
	c = float(raw_input("Podaj c zbioru A "))
	A_x1 = float(raw_input("Podaj x1 zbioru A "))
	A_x2 = float(raw_input("Podaj x2 zbioru A "))
	A_x3 = float(raw_input("Podaj x3 zbioru A "))
	A_x4 = float(raw_input("Podaj x4 zbioru A "))
	A_x5 = float(raw_input("Podaj x5 zbioru A "))

	x1_A = licz(A_x1,a,b,c)
	x2_A = licz(A_x2,a,b,c)
	x3_A = licz(A_x3,a,b,c)
	x4_A = licz(A_x4,a,b,c)
	x5_A = licz(A_x5,a,b,c)

	a = float(raw_input("Podaj a zbioru B "))
	b = float(raw_input("Podaj b zbioru B "))
	c = float(raw_input("Podaj c zbioru B "))
	B_x1 = float(raw_input("Podaj x1 zbioru B "))
	B_x2 = float(raw_input("Podaj x2 zbioru B "))
	B_x3 = float(raw_input("Podaj x3 zbioru B "))
	B_x4 = float(raw_input("Podaj x4 zbioru B "))
	B_x5 = float(raw_input("Podaj x5 zbioru B "))

	x1_B = licz(B_x1,a,b,c)
	x2_B = licz(B_x2,a,b,c)
	x3_B = licz(B_x3,a,b,c)
	x4_B = licz(B_x4,a,b,c)
	x5_B = licz(B_x5,a,b,c)

	print "przekroj zbioru A, B to:"
	print "x1: ", min(x1_A, x1_B)
	print "x2: ", min(x2_A, x2_B)
	print "x3: ", min(x3_A, x3_B)
	print "x4: ", min(x4_A, x4_B)
	print "x5: ", min(x5_A, x5_B)
elif i==3:
	a = float(raw_input("Podaj a zbioru A "))
	b = float(raw_input("Podaj b zbioru A "))
	c = float(raw_input("Podaj c zbioru A "))
	A_x1 = float(raw_input("Podaj x1 zbioru A "))
	A_x2 = float(raw_input("Podaj x2 zbioru A "))
	A_x3 = float(raw_input("Podaj x3 zbioru A "))
	A_x4 = float(raw_input("Podaj x4 zbioru A "))
	A_x5 = float(raw_input("Podaj x5 zbioru A "))

	x1_A = licz(A_x1,a,b,c)
	x2_A = licz(A_x2,a,b,c)
	x3_A = licz(A_x3,a,b,c)
	x4_A = licz(A_x4,a,b,c)
	x5_A = licz(A_x5,a,b,c)

	a = float(raw_input("Podaj a zbioru B "))
	b = float(raw_input("Podaj b zbioru B "))
	c = float(raw_input("Podaj c zbioru B "))
	B_x1 = float(raw_input("Podaj x1 zbioru B "))
	B_x2 = float(raw_input("Podaj x2 zbioru B "))
	B_x3 = float(raw_input("Podaj x3 zbioru B "))
	B_x4 = float(raw_input("Podaj x4 zbioru B "))
	B_x5 = float(raw_input("Podaj x5 zbioru B "))

	x1_B = licz(B_x1,a,b,c)
	x2_B = licz(B_x2,a,b,c)
	x3_B = licz(B_x3,a,b,c)
	x4_B = licz(B_x4,a,b,c)
	x5_B = licz(B_x5,a,b,c)

	print "przekroj zbioru A, B to:"
	print "x1: ", max(x1_A, x1_B)
	print "x2: ", max(x2_A, x2_B)
	print "x3: ", max(x3_A, x3_B)
	print "x4: ", max(x4_A, x4_B)
	print "x5: ", max(x5_A, x5_B)
elif i==4:
	a = float(raw_input("Podaj a "))
	b = float(raw_input("Podaj b "))
	c = float(raw_input("Podaj c "))
	x1 = float(raw_input("Podaj x1 "))
	x2 = float(raw_input("Podaj x2 "))
	x3 = float(raw_input("Podaj x3 "))
	x4 = float(raw_input("Podaj x4 "))
	x5 = float(raw_input("Podaj x5 "))

	x1_A = licz(x1,a,b,c)
	x2_A = licz(x2,a,b,c)
	x3_A = licz(x3,a,b,c)
	x4_A = licz(x4,a,b,c)
	x5_A = licz(x5,a,b,c)

	print "dopelnienie zbioru to:"
	print "x1: ", 1 - x1_A
	print "x2: ", 1 - x2_A
	print "x3: ", 1 - x3_A
	print "x4: ", 1 - x4_A
	print "x5: ", 1 - x5_A

	
	

	


