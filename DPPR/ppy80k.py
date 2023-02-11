def a(n):
  if n==0:
    return 1
  if n==1:
    return 3
  if n>1:
    return 3*a(n-1) - 2*a(n-2) + 2**n

b=int(input())
print(a(b))
