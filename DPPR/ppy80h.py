def a(n):
  if n==0:
    return 6
  if n==1:
    return 3
  if n==2:
    return 71
  if n==3:
    return 203
  if n>3:
    return 2*a(n-1) + 15*a(n-2) + 4*a(n-3) - 20*a(n-4)

b=int(input())
print(a(b))
