import numpy as np
myarray = []
with open('cs-en-simple-dictionary.txt') as f:
	lines=f.readlines()
	for line in lines:
		#print (line)
		line = line.replace("\n","")
		myarray.append(line.split(';'))
f.close()

f1=open("./dev-0/in.tsv",'r')
f2=open("./dev-0/out.tsv",'w')
for line in f1.readlines():
	print (line)
	line = line.lower()
	line=line.replace(","," ,")
	line=line.replace("."," .")
	for a,b in myarray:
		line=line.replace(b,a)
		#print (a, b)
	line=line.replace(" ,",",")
	line=line.replace(" .",".")
	f2.write(line)
	print (line)
f1.close()
f2.close()

f1=open("./test-A/in.tsv",'r')
f2=open("./test-A/out.tsv",'w')
for line in f1.readlines():
	print (line)
	line = line.lower()
	line=line.replace(","," ,")
	line=line.replace("."," .")
	for a,b in myarray:
		line=line.replace(b,a)
		#print (a, b)
	line=line.replace(" ,",",")
	line=line.replace(" .",".")
	f2.write(line)
	print (line)
f1.close()
f2.close()
