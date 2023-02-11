import math

for i in range(int(input())):
  a,b = [int(i) for i in input().split()]
  c1=math.sqrt((a*a)+(b*b))
  c2=math.ceil(c1)
  angle1=math.asin(a/c1)
  angle1=round(angle1*180/math.pi)
  angle2=math.asin(b/c1)
  angle2=round(angle2*180/math.pi)
  if angle1<angle2:
    print (c2,angle1)
  else:
    print (c2,angle2)
