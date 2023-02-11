def a(n):
  if n==0:
    return 1
  if n==1:
    return 1
  if n==2:
    return 5
  if n>2:
    return a(n-1) + 4*a(n-2) + 2*a(n-3)

b=int(input())
print(a(b))
