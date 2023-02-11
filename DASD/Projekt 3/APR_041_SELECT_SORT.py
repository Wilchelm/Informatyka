import time

TAB = []

start_time = time.time()

def SELECT_SORT(Tab):  
  # przechodzimy liste 
  for i in range(len(Tab)): 
    # Znajdź minimalny element tablicy.
    min_idx = i 
    # Przeszukiwanie pozostałej prawej części tablicy w celu znalezienia najmniejszego z pozostałych elemntów.
    for j in range(i+1, len(Tab)): 
        if Tab[min_idx] > Tab[j]: 
            min_idx = j 
              
    # Zamien minimum ze wskazanym elementem
    Tab[i], Tab[min_idx] = Tab[min_idx], Tab[i] 
  return Tab

x=int(input())

for i in range(1,x+1):
  TAB = [int(i) for i in input().split()]
  TAB = SELECT_SORT(TAB)
  print (*TAB[0:-1])  
  
print (time.time() - start_time)
