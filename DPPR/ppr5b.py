
suma = 0

b,c = input().split()
b = int(b)
c = int(c)

for i in range(b+1,c):
  if i%2==1:
    suma = suma + i
print (suma)
