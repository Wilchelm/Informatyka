x=[]

for i in range(int(input())):
  a,b,c,d=input().split()
  b=int(b)
  d=int(d)
  x.append((a,b,c,d))
rok1=int(input())
rok2=int(input())
s=input()
x2=[]
x3=[]
x4=[]
for a,b,c,d in x:
  if b>rok1:
    x2.append(a+" "+str(b)+" ("+c+")")
  if 2014-d<rok2:
    x3.append(a+" "+str(b)+" ("+c+")")
  if a[0]==s:
    x4.append(a+" "+str(b)+" ("+c+")")
if len(x2)>0:
  print (*x2)
if len(x3)>0:
  print (*x3)
if len(x4)>0:
  print (*x4)
