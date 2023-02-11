import time
import numpy as np
import pandas
import torch
import math 
from sklearn.linear_model import LogisticRegression
start_time = time.time()

column_names_train = ['Sane', 'Domain', 'Word', 'Frequency']
column_names = ['Domain', 'Word', 'Frequency']

train_tsv = pandas.read_csv('train/train.tsv', sep='\t', header=None, names=column_names_train)
dev_in_tsv = pandas.read_csv('dev-0/in.tsv', sep='\t', header=None, names=column_names)
test_in_tsv = pandas.read_csv('test-A/in.tsv', sep='\t', header=None, names=column_names)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))

def normalize(x):
	x['Domain'].replace("astronomia", 0, inplace=True)
	x['Domain'].replace("matematyka", 1, inplace=True)
	x['Domain'].replace("medycyna", 2, inplace=True)
	x['Domain'].replace("militaria", 3, inplace=True)
	x['Domain'].replace("okultyzm", 4, inplace=True)
	x['Domain'].replace("sport", 5, inplace=True)
	return x;
	
words = ['a', 'ą', 'b', 'c', 'ć', 'd', 'e', 'ę', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'ł', 'm', 'n', 'ń', 'o', 'ó', 'p', 'r', 's', 'ś', 't', 'u', 'w', 'y', 'z', 'ź', 'ż']


word2int = {}
int2word = {}

for i,word in enumerate(words):
    word2int[word] = i
    int2word[i] = word

def count_char(x):
	lis = []
	for i in x['Word']:
		i = str(i).lower()
		pom_count_char = 0
		for i2 in i:
			try:
				pom_count_char += word2int[i2]
			except:
				pom_count_char += 40
		lis.append(pom_count_char)
	x['Word'] = lis
	#print (lis)
	return x


train_tsv = normalize(train_tsv)
dev_in_tsv = normalize(dev_in_tsv)
test_in_tsv = normalize(test_in_tsv)	

train_tsv = count_char(train_tsv)

dev_in_tsv = count_char(dev_in_tsv)
test_in_tsv = count_char(test_in_tsv)


data_train = train_tsv[['Domain', 'Word', 'Frequency']].values
data_train = np.hstack((data_train, np.ones((data_train.shape[0], 1), dtype=data_train.dtype)))
x = torch.tensor(data_train , dtype=torch.float)
y = torch.tensor(train_tsv['Sane'], dtype=torch.float)
w = torch.tensor([0, 0, 0, 0], dtype=torch.float, requires_grad=True)
lr = torch.tensor(0.00001)

#regresion = LogisticRegression()
#regresion.fit(x, y)

gab = 0

for _ in range(100000):
	y_predicted = x @ w
	cost = torch.sum((y_predicted - y) ** 2) / y.size()[0]
	#print (y_predicted)
	#print(_, w, " => ", cost)
	if _ % 1000 == 0:
		print(gab, y_predicted,_, w, " => ", cost)
	cost.backward()
	gab = gab + 1
	with torch.no_grad():
		w = w - lr * w.grad
		w.requires_grad_(True)
w.requires_grad_(False)


data_dev = dev_in_tsv[['Domain', 'Word', 'Frequency']].values
data_dev = np.hstack((data_dev, np.ones((data_dev.shape[0], 1), dtype=data_dev.dtype)))
x_dev = torch.tensor(data_dev, dtype=torch.float)

data_test_in_tsv = test_in_tsv[['Domain', 'Word', 'Frequency']].values
data_test_in_tsv = np.hstack((data_test_in_tsv, np.ones((data_test_in_tsv.shape[0], 1), dtype=data_test_in_tsv.dtype)))
x_test = torch.tensor(data_test_in_tsv , dtype=torch.float)

#y_dev_predicted = regresion.predict(x_dev)
#y_test_predicted = regresion.predict(x_test)

was = 0.08

y_dev_predicted = x_dev @ w
y_test_predicted = x_test @ w
blabla=0
for i in y_dev_predicted:
	if i > was:
		blabla += 1
		print (i)

print (blabla)

bla=0
the_file2 = open('./dev-0/out.tsv', 'w+')
for i in y_dev_predicted:
	faf = i.numpy()
	if faf>was:
		bla+=1
		the_file2.write('1\n')
	else:
		the_file2.write('0\n')	
the_file2.close()

print (bla)

the_file2 = open('./test-A/out.tsv', 'w+')
for i in y_test_predicted:
	faf = i.numpy()
	if faf>was:
		the_file2.write('1\n')
	else:
		the_file2.write('0\n')	
the_file2.close()

print (time.time() - start_time)
