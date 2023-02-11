import time

TAB = []

start_time = time.time()

def BUBBLE_SORT(Tab): 
  n = len(Tab) 
  
  # Przechodzimy całą tablicę w poszukiwaniu najwiekszego elementu i ustawiamy najwiekszy element na ostatnim miejscu.
  for i in range(n-1): 
    # Zakres maleje wraz ze wzrostem i
    for j in range(0, n-i-1):
      # Przechodzimy przez tablice od 0 do n-i-1 oraz zamieniamy miejscamy gdy jest większy.
      #print (i,j)
      # Przesowamy najwiekszy element na koniec.
      if Tab[j] > Tab[j+1]: 
        Tab[j], Tab[j+1] = Tab[j+1], Tab[j] 
  return Tab


x=int(input())

for i in range(1,x+1):
  TAB = [int(i) for i in input().split()]
  TAB = BUBBLE_SORT(TAB)
  print (*TAB[0:-1])  
  
print (time.time() - start_time)
