x=input()
y=0
z=[]
for i in x:
  if y==1:
    z.append(i.lower())
  if y==0:
    z.append(i.upper())
    y=1
print (*z, sep="")
