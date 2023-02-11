file1 = open("./Dane_PR2/pary.txt", "r") 
Lines = file1.readlines() 

pierwsze=[2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97]

for line in Lines: 
    line=line.split()
    x=int(line[0])
    if x>=4:
      if x%2==0:
        for i in pierwsze:
          find = False
          for j in pierwsze:
            if (i+j==x):
              if (i<j):
                print (x,i,j)
                find = True 
                break
              else:
                print (x,j,i)
                find = True 
                break
          if find: 
            break 
