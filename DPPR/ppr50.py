def syspoz(licz, baza=2):
  digits = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  cyfry = ''
  if licz == 0: cyfry='0'
  while licz!=0:
    r=licz%baza
    cyfry += digits[r]
    licz = licz//baza
  return cyfry[::-1]

n=int(input())
input()
podstawy = input().split()
for p in podstawy:
  print (syspoz(n, int(p)))
