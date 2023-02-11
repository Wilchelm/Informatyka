x = input().split()

a=0
b=0

for i in x:
  if int(i)!=0:
    a=a+1
    b=b+int(i)
  else:
    break
print ("%.2f" % (b/a))
