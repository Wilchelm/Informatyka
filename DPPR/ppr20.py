n=int(input())
for i in range(n):
  s=input()
  pom=str(len(s))+" "
  numbers = sum(c.isdigit() for c in s)
  letters = sum(c.isalpha() for c in s)
  pom+=str(letters)+" "
  pom+=str(numbers)
  print (pom)
