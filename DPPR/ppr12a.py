input()

skarby=[int(i3) for i3 in input().split()]
x=int(input())
for i in range(0,x):
  x,y = [int(i2) for i2 in input().split()]
  suma=0
  for i4 in range(x-1,y):
    suma=suma+skarby[i4]
  print (suma)
