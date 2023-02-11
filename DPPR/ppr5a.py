

def loga(w,p):
  if w==1: return 0
  pp=p
  wykladnik=1
  while w>pp:
    pp=pp*p
    wykladnik+=1 
  return wykladnik 
  
  
  
  
a,b = input().split()

a=int(a)
b=int(b)

print (loga(a,b))
