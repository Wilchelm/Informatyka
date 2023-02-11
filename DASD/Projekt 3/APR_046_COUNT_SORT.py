import time

TAB = []

start_time = time.time()

def COUNT_SORT(Tab):
  size = len(Tab)
  k=max(Tab)+2
  output = [0 for i in range(size)] 

  # Inicjalizujemy tablice z zerami
  count = [0 for i in range(k)]

  # Zliczamy ile jest jakich liczb
  for i in Tab: 
    count[i] += 1
  # Dodajemy do obecnej liczby liczbę z poprzedniego elementu
  for i in range(k): 
    count[i] += count[i-1] 

  # Ustawianie na odpowiednim miejscu
  for i in range(size): 
    output[count[Tab[i]]-1] = Tab[i] 
    count[Tab[i]] -= 1
    
  return output
  
 
x=int(input())

for i in range(1,x+1):
  TAB = [int(i) for i in input().split()]
  TAB = COUNT_SORT(TAB)
  print (*TAB[0:-1])  
  
print (time.time() - start_time)
