def czy_pierwsza(n):
  if n==0:
    return False
  if n==1:
    return False  
  for i in range(2, n):
    if n % i == 0:
      return False
  return True
    
def funkjca(a,b,c):
  pom=0
  if (czy_pierwsza(a)==True):
    pom+=1
  if (czy_pierwsza(b)==True):
    pom+=1
  if c==a*b:
    pom+=1
  if pom==3:
    print ("TAK")
  if pom!=3: 
    print ("NIE")  
    
a,b,c = [int(i) for i in input().split()]

funkjca(a,b,c)
