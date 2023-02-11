w,h = [int(i) for i in input().split()]
Matrix = [0 for y in range(w)]
for x in range(w):
  Matrix[x]=input().split()
Matrix2=list(reversed(list(zip(*Matrix))))
for i1 in range(h):
    print (*Matrix2[i1])
