import operator
from threading import Thread

def unique(list1): 
  
    # intilize a null list 
    unique_list = [] 
      
    # traverse for all elements 
    for x in list1: 
        # check if exists in unique_list or not 
        if x not in unique_list: 
            unique_list.append(x)
        else:
            print (x) 
    return unique_list

def my_sort(b, start, stop):
    for i in b[start:stop]:
        print (type(i), i, b[b.index(i)+1])

'''
        for j in b[start:stop]:
            if i[0] == j[0]:
                if j[1] == 0:
                    if i[1] != 0:
                        print (i,j)
                        b.remove(j)
                        print (len(b))
'''
a = open('word_frequency.txt','r')
b=[]
c = open('slowa.txt','r')

for line in a.readlines():
    line=line.replace('\n','')
    line=line.split('\t')
    line[1]=int(line[1])
    b.append(line)
a.close()

for line in c.readlines():
    line=line.replace('\n','')
    line=line+"\t0"
    line=line.split('\t')
    line[1]=int(line[1])
    b.append(line)
c.close()

last = len(b)-2
b.sort(key = operator.itemgetter(0))

print (b)

#my_sort(b, 0, last+1)

i = 0

length = len(b) - 1 
'''
while i<length:
    pom1 = b[i]
    pom2 = b[i+1]
    if pom1 == pom2:
        b.remove(pom2)
        length = length - 1
    if pom1[0] == pom2[0]:
        if pom2[1] == 0:
            if pom1[1] != 0:
                b.remove(pom2)
                length = length - 1
    print (pom1, pom2)
        
    i+=1
'''
print (length+1, '\t' ,len(b))
'''
q = open('dane/waga0.txt','w+')
w = open('dane/waga-1.txt','w+')
e = open('dane/waga-2.txt','w+')
r = open('dane/waga-3.txt','w+')
t = open('dane/waga-4.txt','w+')
z = open('dane/waga-5.txt','w+')

for x in b:
    y = str(x[0]) + "\n"
    if (x[1] > 100000):
        z.write(y)
    if (50000 < x[1] <= 100000):
        t.write(y)
    if (10000 < x[1] <= 50000):
        r.write(y)
    if (1000 < x[1] <= 10000):
        e.write(y)
    if (1 < x[1] <= 1000):
        w.write(y)
    else:
        q.write(y)

q.close()
w.close()
e.close()
r.close()
t.close()
z.close()
'''
