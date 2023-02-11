import math

tab=[]
for x in range(int(input())):
  p,q,r = [int(i) for i in input().split()]
  tab.append((p,q,r))
for x2 in range(int(input())):
  a,b = [int(i) for i in input().split()]
  odleglosc=math.sqrt((tab[b-1][0]-tab[a-1][0])**2+(tab[b-1][1]-tab[a-1][1])**2)
  wieksze_pole=0
  pole1=tab[a-1][2]**2*3.14
  pole2=tab[b-1][2]**2*3.14
  if pole1>pole2:
    wieksze_pole=pole1
  else:
    wieksze_pole=pole2
  print ("%.2f %.2f" % (odleglosc,wieksze_pole))
