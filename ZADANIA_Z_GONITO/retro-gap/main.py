#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import numpy as np 
import pandas
from nltk import bigrams
from nltk import ConditionalFreqDist
from nltk.probability import ConditionalProbDist, ELEProbDist

start_time = time.time()


train_tsv = pandas.read_csv('./train/train.tsv', sep='\t', header=None)

text = "" 
for line in train_tsv.loc[:,4]:
	line = line.lower()
	text += line
text =  text.split()
print ("split done")
bigrams = bigrams(text)
print ("bigrams done")
cfdist = ConditionalFreqDist(bigrams)
bigrams.close()
print ("ConditionalFreqDist done")
cpdist = ConditionalProbDist(cfdist, ELEProbDist)
print ("ConditionalProbDist done")
print (time.time() - start_time)
text = ""

dev_0 = 100
the_file2 = open('./dev/out.tsv', 'w+')
with open('./dev/in.tsv') as f:
	for line in f:
		line = line.lower()
		dev_0-=1
		print (dev_0)
		x = line.split('	')
		y = x[2].split()
		pom2 = ''
		#pom3 = []
		for i in cfdist[y[-1]].most_common(10):
			pom2 += str(i[0])+':'+str(cpdist[y[-1]].logprob(i[0])) + ' '
			#pom3.append(cpdist[y[-1]].logprob(i[0]))
		#pom4 = (np.log(np.log(np.exp(1.0-np.exp(pom3).sum()))))
		pom2 = pom2[:-1]
		pom2 = pom2 + ' :-0.95\n'
		if pom2 == ' :-0.95\n':
			pom2 = ':-0.95\n'
		#pom2 = pom2 + ' :' + str(pom4)+'\n'
		#if pom2 == ' :0.0\n':
		#	pom2 = ':0.0\n'
		#if pom2 == ' :1.0\n':
		#	pom2 = ':1.0\n'
		#pom2 = pom2.replace(' :-inf','')
		the_file2.write(pom2)
f.close()
the_file2.close()

print (time.time() - start_time)
