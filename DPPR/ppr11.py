def nwd(a, b):
    while b:
        temp = a
        a = b
        b = temp%b
    return a
'''
def nwd_tab(tab):
  nwdv=tab[0]
  for i in range(0,len(tab)-1):
    nwdv = nwd(nwdv, tab[i])
  return nwdv

x = [int(i) for i in input().split()]
pom=0
tab_pom=[]

suma=0
'''
x = [int(i) for i in input().split()]
pom1=0
pom2=0

suma=0

for i in range(0,len(x)-1):
  if i==0: pom1=x[i]
  if i==1: pom2=x[i]
  if i>1:
    if x[i]==1:
      suma=suma+nwd(pom1,pom2)
    else:
      pom1=pom2
      pom2=x[i]
print (suma)

'''
for i2 in x:
  if i2==0:
    print (suma)
    quit()
  if i2==1:
    if len(tab_pom)!=0:
    	suma=suma+nwd_tab(tab_pom)
    tab_pom.clear()
    pom=0
  else:
    tab_pom.append(i2)
'''
