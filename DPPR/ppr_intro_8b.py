
suma = 0

b,c = input().split()
b = int(b)
c = int(c)

x = input().split()

for i in x:
  if int(i) == b:
    suma = suma + 1
print (suma)
