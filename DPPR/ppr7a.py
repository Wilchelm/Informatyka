input()
x=input().split()
x2=[]
for i in range(2,len(x),3):
  x2.append(x[i])
print (*x2[::-1])
