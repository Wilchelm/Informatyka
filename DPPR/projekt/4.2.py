file1 = open("./Dane_PR2/pary.txt", "r") 
Lines = file1.readlines() 

for line in Lines: 
    line=line.split()
    x=line[1]
    maks1=1
    maks2=""
    pom1=""
    pom2=1
    pierwsza=""
    for i in range(0,len(x)-1):
      if pierwsza=="":
        pierwsza=x[i]
      if (x[i]==x[i+1]):
        pom2+=1
        pom1=x[i]
        if pom2>maks1:
          maks1=pom2
          maks2=x[i]
      else:
        pom2=1
    if maks1==1:
      print (pierwsza,"1")
    if maks1>1:
      print (maks2*maks1,maks1)
