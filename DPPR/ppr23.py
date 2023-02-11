n=int(input())
pom=[]
pom2=[]
for i in range(n):
  pom.append(int(input()))

pom.sort()  

for i in range(0,len(pom)-1):
  if pom[i]==pom[i+1]:
    pom2.append(pom[i])
      
for i in sorted(set(pom2)):
  print(i)
