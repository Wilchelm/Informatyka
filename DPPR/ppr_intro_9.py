a,b,c = input().split()
a = int(a)
b = int(b)
c = int(c)
x=[]
if c>=b:
  for i in range(b,c+1):
    if i%a==0:
      x.append(i)
  print (*x)
else:
  for i in range(c,b+1):
    if i%a==0:
      x.append(i)
  y=x[::-1]
  print (*y)
