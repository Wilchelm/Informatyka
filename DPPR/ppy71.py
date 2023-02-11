P=int(input())
n=int(input())

if n==0:
  print(0)
if n!=0:
  pom=0
  for i in range(0,n):
    a,b = [int(i) for i in input().split()]
    if (a*b<P):
      pom+=1
  print (pom)
