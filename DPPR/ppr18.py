x=int(input())
for i in range(1,x+1):
  pom1=input()
  pom2=pom1[::-1]
  if pom1==pom2:
    print(pom1,"==",pom2,sep="")
  if pom1!=pom2:
    print(pom1,"!=",pom2,sep="")
