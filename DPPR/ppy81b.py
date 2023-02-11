def b(n,k):
  if k==0:
    return 1
  if k==n:
    return 1
  if k>n:
    return 0
  if 0<k<n:
    return b(n-1,k) + b(n-1,k-1)

a,c=[int(i) for i in input().split()]
print(b(a,c))
