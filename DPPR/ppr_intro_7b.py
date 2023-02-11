input()
x=input().split()
y=[]
for i in x:
  if i.isupper()==True:
    y.append(i.lower())
  if i.islower()==True:
    y.append(i.upper())
print (*y,sep="")
