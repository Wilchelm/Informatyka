def b(n,k):
  if k==1:
    return n
  if 2*k-1==n:
    return 1
  if n<2*k-1:
    return 0
  if k > 1: 
    if n > 2*k-1:
      return b(n-2,k-1) + b(n-1,k)

a,c=[int(i) for i in input().split()]
print(b(a,c))
