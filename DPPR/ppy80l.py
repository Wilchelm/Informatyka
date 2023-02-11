def a(n):
  if n==1:
    return 1
  if n>1:
    return 2*a(n-1) + 7*n**2

b=int(input())
print(a(b))
