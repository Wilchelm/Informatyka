def a(n):
  if n==1:
    return 5
  if n==2:
    return 13
  if n>2:
    return 2*a(n-1) + 3*a(n-2)

b=int(input())
print(a(b))
