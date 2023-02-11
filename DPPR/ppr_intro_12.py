input()
x = input().split()
maksymalna = 0
for i in x:
  if int(i)>maksymalna:
    maksymalna=int(i)
pom=0 
for i in x:
  if int(i)==maksymalna:
    pom=pom+1
print (pom)
