lista=[]
for i in range(1,int(input())+1):
  lista.append(input())
x=input()
suma=0
for j in lista:
  if j==x: suma+=1
print (suma) 
