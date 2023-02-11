def a(n):
  if n==0:
    return 0
  if n==1:
    return 1
  if n==2:
    return 2
  if n>2:
    return 2*a(n-1) + 3*a(n-3)

b=int(input())
print(a(b))
