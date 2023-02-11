def a(n):
  if n==0:
    return 1
  if n>0:
    return a(n-1)+n

b=int(input())
print(a(b))
