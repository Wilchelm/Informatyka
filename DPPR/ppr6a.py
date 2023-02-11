x=int(input())
for i in range(0,x):
  a=input().split()
  b=int(a[0])
  c=int(a[1])
  
  if (b<c):
    if (a[2]=="+"):
      pom=0
      for j in range(b,c+1):
        pom=pom+j
      print (pom)
    if (a[2]=="-"):
      pom=0
      for j in range(b,c+1):
        pom=pom-j
      print (pom)
    if (a[2]=="*"):
      pom=1
      for j in range(b,c+1):
        pom=pom*j
      print (pom)
  if (c<b):
    if (a[2]=="+"):
      pom=0
      for j in range(c,b+1):
        pom=pom+j
      print (pom)
    if (a[2]=="-"):
      pom=0
      for j in range(c,b+1):
        pom=pom-j
      print (pom)
    if (a[2]=="*"):
      pom=1
      for j in range(c,b+1):
        pom=pom*j
      print (pom)
