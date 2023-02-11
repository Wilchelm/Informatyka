a=input()
a=int(a)
if a%4==0:
  if a%100!=0:
    print ("Yes")
elif a%400==0:
  print ("Yes")
else:
  print ("No")
