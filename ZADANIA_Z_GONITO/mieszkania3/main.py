import time
import numpy as np
import pandas
import torch

start_time = time.time()

column_names = ['Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku', 'Piętro', 'Typ zabudowy', 'Okna', 'Materiał budynku', 'Rok budowy', 'Forma własności', 'Forma kuchni', 'Stan', 'Stan instalacji', 'Głośność', 'Droga dojazdowa', 'Stan łazienki', 'Powierzchnia działki w m2', 'opis']

train_tsv = pandas.read_csv('train/train.tsv', sep='\t', header=0, usecols=['cena', 'Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku', 'Piętro', 'Typ zabudowy', 'Okna', 'Materiał budynku', 'Rok budowy', 'Forma własności', 'Forma kuchni', 'Stan', 'Stan instalacji', 'Głośność', 'Droga dojazdowa', 'Stan łazienki', 'Powierzchnia działki w m2', 'opis'])
dev_in_tsv = pandas.read_csv('dev-0/in.tsv', sep='\t', header=None, names=column_names)
test_in_tsv = pandas.read_csv('test-A/in.tsv', sep='\t', header=None, names=column_names)

def train_normalize(x):
	x = x.fillna(0)
	x.drop( x[ x['cena'] > 5000000 ].index , inplace=True)
	x.drop( x[ x['cena'] < 50000 ].index , inplace=True)
	x.drop( x[ x['Powierzchnia w m2'] > 1000 ].index , inplace=True)
	x['Piętro'].replace(["parter", " parter"], 0, inplace=True)
	x['Piętro'].replace(["niski parter", " niski parter"], 0, inplace=True)
	x['Piętro'].replace(["poddasze", " poddasze"], 20, inplace=True)
	x['Miejsce parkingowe'].replace(["brak miejsca parkingowego", " brak miejsca parkingowego"], 0, inplace=True)
	x['Miejsce parkingowe'].replace(["parking strzeżony", " parking strzeżony"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["pod wiatą", " pod wiatą"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["przynależne na ulicy", " przynależne na ulicy"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["w garażu", " w garażu"], 1, inplace=True)
	return x;

def data_normalize(x):
	x = x.fillna(0)
	x.drop( x[ x['Powierzchnia w m2'] > 1000 ].index , inplace=True)
	x['Piętro'].replace(["parter", " parter"], 0, inplace=True)
	x['Miejsce parkingowe'].replace(["brak miejsca parkingowego", " brak miejsca parkingowego"], 0, inplace=True)
	x['Miejsce parkingowe'].replace(["parking strzeżony", " parking strzeżony"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["pod wiatą", " pod wiatą"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["przynależne na ulicy", " przynależne na ulicy"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["w garażu", " w garażu"], 1, inplace=True)
	x['Piętro'].replace(["niski parter", " niski parter"], 0, inplace=True)
	x['Piętro'].replace(["poddasze", " poddasze"], 20, inplace=True)
	return x;

train_tsv = train_normalize(train_tsv)

dev_in_tsv = data_normalize(dev_in_tsv)
test_in_tsv = data_normalize(test_in_tsv)	

data_train = train_tsv[['Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku']].values
data_train = np.hstack((data_train, np.ones((data_train.shape[0], 1), dtype=data_train.dtype)))
x = torch.tensor(data_train , dtype=torch.float)
y = torch.tensor(train_tsv['cena'], dtype=torch.float)
w = torch.tensor([0, 0, 0, 0, 0], dtype=torch.float, requires_grad=True)
lr = torch.tensor(0.00000001)

for _ in range(100000):
	y_predicted = x @ w
	cost = torch.sum((y_predicted - y) ** 2) / y.size()[0]
	#print(_, w, " => ", cost)
	cost.backward()
	with torch.no_grad():
		w = w - lr * w.grad
		w.requires_grad_(True)
w.requires_grad_(False)

data_dev = dev_in_tsv[['Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku']].values
data_dev = np.hstack((data_dev, np.ones((data_dev.shape[0], 1), dtype=data_dev.dtype)))
x_dev = torch.tensor(data_dev, dtype=torch.float)

data_test_in_tsv = test_in_tsv[['Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku']].values
data_test_in_tsv = np.hstack((data_test_in_tsv, np.ones((data_test_in_tsv.shape[0], 1), dtype=data_test_in_tsv.dtype)))
x_test = torch.tensor(data_test_in_tsv , dtype=torch.float)

y_dev_predicted = x_dev @ w
y_test_predicted = x_test @ w

np.savetxt(f'./dev-0/out.tsv', y_dev_predicted.numpy(), '%.0f')
np.savetxt(f'./test-A/out.tsv', y_test_predicted.numpy(), '%.0f')

print (time.time() - start_time)
