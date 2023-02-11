input()
a=input().split()
b=[]
for i in a:
  if i.isupper()==True:
    b.append(i)
print (*b[::-1])
