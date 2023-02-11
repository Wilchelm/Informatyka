#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time, pandas, re

start_time=time.time()

def ishere(what, where):
	if what.lower() in where.lower():
		return True
	else:
		return False

def findhere(what, where):
	if ishere(what, where) is True:
		return what

def findsomething(line, lista1, lista2):
	listas = []
	for i in lista1:
		pom = findhere(str(i).lower(), str(line).lower())
		if pom is not None:
			#return lista2[lista1.index(i)]
			listas.append(lista2[lista1.index(i)])
	y=sum(listas)/len(listas)	
	return y

def myRegex(line):
	count = []
	for number in re.findall(r"(1[89][0-9][0-9]|20[0-9][0-9])", line):
		count.append(float(number))
	return sum(count)/len(count)

#train_in_tsv = pandas.read_csv('train/train.tsv', sep='\t', header=None)

#x = train_in_tsv[[0,1]]
#y = train_in_tsv[[2,3,4]]
#x=x.mean(axis=1)
#list_x=x.values.tolist()
#list_y1=y[y.columns[0]].values.tolist()
#list_y2=y[y.columns[2]].values.tolist()

#del train_in_tsv
#del x
#del y

dev0_in_tsv = open('dev-0/in.tsv', 'r')
dev0_out_tsv = open('dev-0/out.tsv', 'w')
jint = 0
jList=[]
jList.append(float(1913))
for i1 in dev0_in_tsv.readlines():
	try:
		x1 = float(myRegex(i1))
		jList.append(x1)
	except:
		x1 = 0
	if x1==0: 
		x=float(sum(jList)/len(jList))
		#x = findsomething(i1, list_y1, list_x)
		dev0_out_tsv.write('%.00000000000f\n' % x)
		jint=jint+1
		print(jint, x)
	else:
		dev0_out_tsv.write('%.00000000000f\n' % x1)
		jint=jint+1
		print(jint, x1)
	
print ('Done dev0!')
dev0_in_tsv.close()
dev0_out_tsv.close()
print (sum(jList)/len(jList),len(jList))

dev1_in_tsv = open('dev-1/in.tsv', 'r')
dev1_out_tsv = open('dev-1/out.tsv', 'w')
jint = 0
jList1=[]
jList1.append(float(1942))
for i1 in dev1_in_tsv.readlines():
	try:
		x1 = float(myRegex(i1))
		jList1.append(x1)
	except:
		x1 = 0
	if x1==0: 
		x=float(sum(jList1)/len(jList1))
		#x = findsomething(i1, list_y1, list_x)
		dev1_out_tsv.write('%.00000000000f\n' % x)
		jint=jint+1
		print(jint, x)
	else:
		dev1_out_tsv.write('%.00000000000f\n' % x1)
		jint=jint+1
		print(jint, x1)
print ('Done dev1')
dev1_in_tsv.close()
dev1_out_tsv.close()
print (sum(jList1)/len(jList1),len(jList1))

testA_in_tsv=open('test-A/in.tsv', 'r')
testA_out_tsv=open('test-A/out.tsv', 'w')
jint = 0
jList2=[]
jList2.append(float(1932))
for i1 in testA_in_tsv.readlines():
	try:
		x1 = float(myRegex(i1))
		jList2.append(x1)
	except:
		x1 = 0
	if x1==0: 
		x=float(sum(jList2)/len(jList2))
		#x = findsomething(i1, list_y1, list_x)
		testA_out_tsv.write('%.00000000000f\n' % x)
		jint=jint+1
		print(jint, x)
	else:
		testA_out_tsv.write('%.00000000000f\n' % x1)
		jint=jint+1
		print(jint, x1)

print ('Done testA!')
testA_in_tsv.close()
testA_out_tsv.close()
print (sum(jList2)/len(jList2),len(jList2))

print (time.time() - start_time)
