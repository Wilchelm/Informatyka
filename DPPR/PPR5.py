import math 

a=input()
b=input()
xa,ya=a.split()
xa=int(xa)
ya=int(ya)
xb,yb=b.split()
xb=int(xb)
yb=int(yb)
x2=(xb-xa)*(xb-xa)
y2=(yb-ya)*(yb-ya)
d=math.sqrt(x2+y2)
print("%.1f" % d)
