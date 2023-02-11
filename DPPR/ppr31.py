input()
x=input().split()
input()
y=input().split()

for i in y:
  while i in x:
    x.remove(i)
  print(*x)
