x,y = input().split()
x=int(x)
y=int(y)
input()

suma=0
c=input().split()
j=0

for i in c:
  j=int(i)
  if (x<=j<=y):
    suma=0
  else:
    if(j<x):
      suma=suma-j+x
    if(j>y):
      suma=suma+j-y
print (suma)
