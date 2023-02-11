def a(n):
  if n==0:
    return 2
  if n==1:
    return 1
  if n>0:
    return 3*a(n-2) + 3**n

b=int(input())
print(a(b))
