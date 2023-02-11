import time
import numpy as np
import pandas
import torch
from torch import nn
from torch import optim
import torch
import math 
from sklearn.linear_model import LogisticRegression
from sklearn import preprocessing
from scipy.special import softmax
start_time = time.time()

column_names_train = ['Sane', 'Domain', 'Word', 'Frequency']
column_names = ['Domain', 'Word', 'Frequency']

train_tsv = pandas.read_csv('train/train.tsv', sep='\t', header=None, names=column_names_train)
dev_in_tsv = pandas.read_csv('dev-0/in.tsv', sep='\t', header=None, names=column_names)
test_in_tsv = pandas.read_csv('test-A/in.tsv', sep='\t', header=None, names=column_names)

def sigmoid(x):
  return 1 / (1 + math.exp(-x))
	
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

#---------------------------------------------------

train_tsv = count_char(train_tsv)
dev_in_tsv = count_char(dev_in_tsv)
test_in_tsv = count_char(test_in_tsv)

#---------------------------------------------------

for col in ['Domain']:
    train_tsv[col] = train_tsv[col].astype('category')

data_train1 = train_tsv['Sane'].values
data_train2 = train_tsv['Domain'].cat.codes.to_numpy()
data_train3 = train_tsv['Word'].values
data_train4 = train_tsv['Frequency'].values
data_train2 = softmax(data_train2)
data_train3 = softmax(data_train3)
data_train4 = softmax(data_train4)
data_train5 = np.ones(data_train1.shape)

data = {'Sane': data_train1,
        'Domain': data_train2,
        'Word': data_train3,
        'Frequency':  data_train4,
        'Bias': data_train5}
df = pandas.DataFrame(data) 

#-----------------------------------------------------

habak = 0
def return_torch():
    global habak
    if (habak > 44343):
        habak = 0 
    a1=df['Domain'].iat[habak]
    b1=df['Word'].iat[habak]
    c1=df['Frequency'].iat[habak]
    d1=df['Bias'].iat[habak]
    kum = []
    kum.append(a1)
    kum.append(b1)
    kum.append(c1)
    kum.append(d1)

    x = torch.tensor(kum,dtype=torch.float)
    y = torch.tensor(df['Sane'].iat[habak], dtype=torch.float)
    habak = habak + 1
    return x, y

#-------------------------------------------------------

lr = 0.0001

model=nn.Sequential(
        nn.Linear(4,56),
        nn.ReLU(),
        nn.Linear(56,1),
        nn.Sigmoid()
)

criterion = nn.MSELoss()

#optimizer = optim.SGD(
#        model.parameters(),
#        lr=lr,
#        momentum=0.9)

optimizer = optim.Adam(model.parameters())

minibatch_size = 250
#alpha = torch.tensor(0.00000001)
'''
for _ in range(1000000):
    optimizer.zero_grad()
    minibatches = [return_torch() for _ in range(minibatch_size)]
    xb = torch.stack([x[0] for x in minibatches])
    yeb = torch.stack([y[1] for y in minibatches])
    #print(xb, yeb)
    #x, ye = get_item() 
    y = torch.squeeze(model(xb))
    loss = criterion(y,yeb)
    print(_ , loss)
    loss.backward()

    optimizer.step()


torch.save(model.state_dict(), './model')
'''

model.load_state_dict(torch.load('./model'))
model.eval()
#--------------------------------------------------------
#--------------------------------------------------------

for col in ['Domain']:
    dev_in_tsv[col] = dev_in_tsv[col].astype('category')

data_train2 = dev_in_tsv['Domain'].cat.codes.to_numpy()
data_train3 = dev_in_tsv['Word'].values
data_train4 = dev_in_tsv['Frequency'].values
data_train2 = softmax(data_train2)
data_train3 = softmax(data_train3)
data_train4 = softmax(data_train4)
data_train5 = np.ones(data_train2.shape)

data = {'Domain': data_train2,
        'Word': data_train3,
        'Frequency':  data_train4,
        'Bias': data_train5}
df = pandas.DataFrame(data)

a1=torch.tensor(df['Domain'],dtype=torch.float)
b1=torch.tensor(df['Word'], dtype=torch.float)
c1=torch.tensor(df['Frequency'], dtype=torch.float)
d1=torch.tensor(df['Bias'], dtype=torch.float)

x_dev = torch.stack((a1,b1,c1,d1),0)

#---------------------------------------------------------------------

for col in ['Domain']:
    test_in_tsv[col] = test_in_tsv[col].astype('category')

data_train2 = test_in_tsv['Domain'].cat.codes.to_numpy()
data_train3 = test_in_tsv['Word'].values
data_train4 = test_in_tsv['Frequency'].values
data_train2 = softmax(data_train2)
data_train3 = softmax(data_train3)
data_train4 = softmax(data_train4)
data_train5 = np.ones(data_train2.shape)

data = {'Domain': data_train2,
        'Word': data_train3,
        'Frequency':  data_train4,
        'Bias': data_train5}
df = pandas.DataFrame(data)

a1=torch.tensor(df['Domain'],dtype=torch.float)
b1=torch.tensor(df['Word'], dtype=torch.float)
c1=torch.tensor(df['Frequency'], dtype=torch.float)
d1=torch.tensor(df['Bias'], dtype=torch.float)

x_test = torch.stack((a1,b1,c1,d1),0)


y_dev_predicted = model(x_dev.t())
y_test_predicted = model(x_test.t())

for i in y_dev_predicted:
    print (i)
waga = 0
bla=0
the_file2 = open('./dev-0/out.tsv', 'w+')
for i in y_dev_predicted:
	if i>waga:
		bla+=1
		the_file2.write('1\n')
	else:
		the_file2.write('0\n')	
the_file2.close()

print (bla)

the_file2 = open('./test-A/out.tsv', 'w+')
for i in y_test_predicted:
	if i>waga:
		the_file2.write('1\n')
	else:
		the_file2.write('0\n')	
the_file2.close()

print (time.time() - start_time)
