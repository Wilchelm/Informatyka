def a(n):
  if n==0:
    return 1
  if n==1:
    return -9
  if n>1:
    return -6*a(n-1)-9*a(n-2)

b=int(input())
print(a(b))
