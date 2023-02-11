a,b=input().split()
a=int(a)
b=int(b)
x=[int(s) for s in input().split()]
y=range(1,a+1)
max_name=0
max_var=0
for i in y:
  print (i,": ",x.count(i),sep="")
  if x.count(i)>max_var:
    max_var=x.count(i)
    max_name=i;
print (max_name)
