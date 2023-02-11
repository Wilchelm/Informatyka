import math

def szyfr(s):
  pom=""
  if len(s)%2==0:
    for i in range(1,len(s),2):
      pom+=s[i]
      pom+=s[i-1]
  if len(s)%2==1:
    for i in range(1,len(s)-1,2):
      pom+=s[i]
      pom+=s[i-1]
    pom+=s[len(s)-1]
  print (pom)
    
  
x=input()
szyfr(x)
