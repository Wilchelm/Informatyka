n=int(input())
for i in range(n):
  a,b,c=input().split()
  if b=="+":
    print (int(a)+int(c))
  if b=="*":
    print (int(a)*int(c))
  if b=="-":
    print (int(a)-int(c))
  
