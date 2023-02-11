input()
a = input().split()
b=[]
c=0

for i in a:
  i = int(i)
  if c%2==1:
    b.append(i)
  c=c+1
  
d=b[::-1]
print(*d)
