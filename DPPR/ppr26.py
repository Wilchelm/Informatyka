def nwd_i(a, b):
    while b:
        temp = a
        a = b
        b = temp%b
    return a
    
for i in range(int(input())):
  lista=[int(i2) for i2 in input().split()]
  maks=lista[0]
  
  for i in lista:
    maks=nwd_i(maks,i)
  print (maks)
