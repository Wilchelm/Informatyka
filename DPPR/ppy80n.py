def a(n):
  if n==0:
    return 0
  if n>0:
    return a(n-1) + 7*n

b=int(input())
print(a(b))
