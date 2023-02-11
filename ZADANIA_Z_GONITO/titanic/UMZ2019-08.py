#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import numpy as np 
import pandas
from sklearn.neural_network import MLPClassifier
start_time = time.time()

def normalize(a):
	a['Sex'] = a['Sex'].replace('male',1)
	a['Sex'] = a['Sex'].replace('female',0)

column_names = ['PassengerId','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked']
train_tsv = pandas.read_csv('train/train.tsv', sep='\t', header=0, usecols=['Survived','PassengerId','Pclass','Name','Sex','Age','SibSp','Parch','Ticket','Fare','Cabin','Embarked'])
dev_in_tsv = pandas.read_csv('dev-0/in.tsv', sep='\t', header=None, names=column_names)
test_in_tsv = pandas.read_csv('test-A/in.tsv', sep='\t', header=None, names=column_names)

x = train_tsv[['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]
y = train_tsv['Survived']

x=x.fillna(0)
x['Sex'] = x['Sex'].replace('male',1)
x['Sex'] = x['Sex'].replace('female',0)
x['Embarked'] = x['Embarked'].replace('S',1)
x['Embarked'] = x['Embarked'].replace('Q',2)
x['Embarked'] = x['Embarked'].replace('C',3)

x_dev = dev_in_tsv[['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]

x_dev=x_dev.fillna(0)
x_dev['Sex'] = x_dev['Sex'].replace('male',1)
x_dev['Sex'] = x_dev['Sex'].replace('female',0)
x_dev['Embarked'] = x_dev['Embarked'].replace('S',1)
x_dev['Embarked'] = x_dev['Embarked'].replace('Q',2)
x_dev['Embarked'] = x_dev['Embarked'].replace('C',3)

x_test = test_in_tsv[['PassengerId','Pclass','Sex','Age','SibSp','Parch','Fare','Embarked']]

x_test=x_test.fillna(0)
x_test['Sex'] = x_test['Sex'].replace('male',1)
x_test['Sex'] = x_test['Sex'].replace('female',0)
x_test['Embarked'] = x_test['Embarked'].replace('S',1)
x_test['Embarked'] = x_test['Embarked'].replace('Q',2)
x_test['Embarked'] = x_test['Embarked'].replace('C',3)


clf = MLPClassifier(hidden_layer_sizes=(1000,1000,1000), max_iter=500, alpha=0.00000001, solver='lbfgs', verbose=10, random_state=21,tol=0.000000001)

clf.fit(x, y)


dev_0 = clf.predict(x_dev)
test_A = clf.predict(x_test)


outF1 = open("dev-0/out.tsv", "w")
for line1 in dev_0:
	outF1.write('%01d\n' % line1)
outF1.close()

outF2 = open("test-A/out.tsv", "w")
for line2 in test_A:
	outF2.write('%01d\n' % line2)
outF2.close()

print (time.time() - start_time)
