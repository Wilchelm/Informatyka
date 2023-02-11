a=int(input())
text = input()
nums = [int(n)**3 for n in text.split(maxsplit = a)]

print (*nums)
  
