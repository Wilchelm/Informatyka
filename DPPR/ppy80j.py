def a(n):
  if n==0:
    return 0
  if n==1:
    return 1
  if n>1:
    return 7*a(n-1) - 10*a(n-2) + 3**n

b=int(input())
print(a(b))
