x=input().split()

pom=0
pom2=0
pom_tab=[]

for i in x:
  if i=="-1":
    quit()
  if i=="0":
    print (*pom_tab)
  if i=="1":
    pom3=pom2/pom
    print ("%.2f" % pom3) 
  if i=="2":
    pom_tab.append(2)
    pom+=1
    pom2+=2
  if i=="3":
    pom_tab.append(3)
    pom+=1
    pom2+=3
  if i=="4":
    pom_tab.append(4)
    pom+=1
    pom2+=4
  if i=="5":
    pom_tab.append(5)
    pom+=1
    pom2+=5
