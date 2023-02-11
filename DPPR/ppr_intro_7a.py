a=int(input())
text = input()
nums = [int(n) for n in text.split(maxsplit = a)]

lista=[]

for i in nums:
  if i%2==0:
    lista.append("P")
  if i%2==1:
    lista.append("N")

print(''.join(map(str, lista)))
  
