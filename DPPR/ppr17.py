def DzielnikiNiewlasciwe(a):
  wynik = []
  for i in range(1, a // 2 + 1):
    if (a % i == 0):
      wynik.append(i)
  if (a > 1):
    wynik.append(a)
  return wynik 

input()
x=[int(i) for i in input().split()]
iterator=int(input())



for i in range (1,iterator+1):
  y=int(input())
  suma=0
  dzielniki=DzielnikiNiewlasciwe(y)
  for i4 in x:
    if i4 in dzielniki:
      suma+=1
  print (suma)
