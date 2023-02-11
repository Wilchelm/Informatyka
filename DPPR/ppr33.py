x=[]

for i in range(int(input())):
  a,b,c,d=input().split()
  c=int(c)
  d=float(d)
  x.append((a,b,c,d))
wiek=int(input())
wzrost=float(input())

x2=[]
x3=[]
for a,b,c,d in x:
  if c>wiek:
    x2.append(a+" "+b)
  if d<wzrost:
    x3.append(a+" "+b)
print (*x2)
print ("----")
print (*x3)
