def a(n):
  if n==1:
    return 1
  if n>1:
    return n**2*a(n-1)

b=int(input())
print(a(b))
