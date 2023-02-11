import math

x=[]
i2=int(input())
for i in range(i2):
  a,b=input().split()
  a=int(a)
  b=int(b)
  x.append((a,b))
  
o=0.0
s=0.0  
for i in range(i2):
  if i<len(x):
    if (len(x)==i+1):
      o+=math.sqrt((x[0][0]-x[i][0])**2+(x[0][1]-x[i][1])**2)
    else:
      o+=math.sqrt((x[i+1][0]-x[i][0])**2+(x[i+1][1]-x[i][1])**2)
for a,b in x:
  s+=math.hypot(a,b)
    

print("%.3f %.3f" % (o,s))
