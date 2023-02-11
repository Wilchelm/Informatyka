for i in range(1,int(input())+1):
  x,y = input().split()
  try:
    y = int(y)
  except:
    y=y
  try:
    x = int(x)
  except:
    x=x
  if type(x)== int and type(y)==int:
    print (x+y)
  if type(x)== str and type(y)==int:
    print (x[y-1])
  if type(x)== int and type(y)==str:
    print (y[x-1])
  if type(x)== str and type(y)==str:
    print (x+y)    
