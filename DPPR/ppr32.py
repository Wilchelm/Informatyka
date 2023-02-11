x={}

for i in range(int(input())):
  a,b = input().split()
  x[a]=b
input()
s=input().split()
s2=""
for i in s:
  try:
    s2=s2+x[i]+" "
  except:
    s2=s2+i+" "
print(s2)
