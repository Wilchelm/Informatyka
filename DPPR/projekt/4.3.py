file1 = open("./Dane_PR2/pary.txt", "r") 
Lines = file1.readlines() 

pom=[]

for line in Lines: 
  line=line.split()
  a=int(line[0])
  b=len(line[1])
  if a==b:
    pom.append((a,line[1]))

min1=0
min2=0
  
zero=0
for i in pom:
   if zero==0:
     count=0
     for j in i[1]:
       count+=ord(j)
     min1=i[0]
     min2=count
     zero+=1
   if zero>0:
     count=0
     for j in i[1]:
       count+=ord(j)
     if min1>i[0]:
       min1=i[0]
       min2=count
     if min2>count and min1==i[0]:
       min1=i[0]
       min2=count  
       
for i in pom:
  count=0
  for j in i[1]:
    count+=ord(j)
  if i[0]==min1 and count==min2:
    print (i[0],i[1])
