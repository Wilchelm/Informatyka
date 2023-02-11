def a(n):
  if n==1:
    return 3
  if n==2:
    return 7
  if n>2:
    return 2*a(n-1) + a(n-2)

b=int(input())
print(a(b))
