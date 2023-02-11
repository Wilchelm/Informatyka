#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import numpy as np 
import pandas
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import OneHotEncoder
from sklearn.naive_bayes import GaussianNB

#numpy.nan_to_num
#wyrzuc odstajace wartosci np cena=0
start_time = time.time()
enc = OneHotEncoder(handle_unknown='ignore')

train_tsv = pandas.read_csv('train/train.tsv', sep='\t', header=None)
dev_in_tsv = pandas.read_csv('dev-0/in.tsv', sep='\t', header=None)
test_in_tsv = pandas.read_csv('test-A/in.tsv', sep='\t', header=None)

for i in train_tsv:
	train_tsv[i] = train_tsv[i].map(ord)

x = train_tsv[[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]]
y = train_tsv[0]

x_dev = dev_in_tsv[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]
x_test = test_in_tsv[[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]]

for i in x_dev:
	x_dev[i] = x_dev[i].map(ord)
for i in x_test:
	x_test[i] = x_test[i].map(ord)

naive_bayes = GaussianNB()
naive_bayes.fit(x, y)


dev_0 = naive_bayes.predict(x_dev)
test_A = naive_bayes.predict(x_test)



outF1 = open("dev-0/out.tsv", "w")
for line1 in dev_0:
	outF1.write('%s\n' % chr(line1))
outF1.close()

outF2 = open("test-A/out.tsv", "w")
for line2 in test_A:
	outF2.write('%s\n' % chr(line2))
outF2.close()

print (time.time() - start_time)
