
suma = 0

b,c = input().split()
b = int(b)
c = int(c)
x=[]

for i in range(b,c+1):
  x.append(i)

for i in x:
  suma = suma + int(i)
print (suma)
