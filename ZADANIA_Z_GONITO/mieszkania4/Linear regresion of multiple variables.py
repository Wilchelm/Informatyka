#!/usr/bin/python3
# -*- coding: utf-8 -*-
import time
import numpy as np 
import pandas
from sklearn.linear_model import LinearRegression

#numpy.nan_to_num
#wyrzuc odstajace wartosci np cena=0
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
	x['Miejsce parkingowe'].replace(["brak miejsca parkingowego", " brak miejsca parkingowego"], 0, inplace=True)
	x['Miejsce parkingowe'].replace(["parking strzeżony", " parking strzeżony"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["pod wiatą", " pod wiatą"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["przynależne na ulicy", " przynależne na ulicy"], 1, inplace=True)
	x['Miejsce parkingowe'].replace(["w garażu", " w garażu"], 1, inplace=True)
	x['Piętro'].replace(["niski parter", " niski parter"], 0, inplace=True)
	x['Piętro'].replace(["poddasze", " poddasze"], 20, inplace=True)
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

#train_tsv['cena'] = train_tsv['cena'].fillna(0)

#train_tsv = train_tsv.fillna(0)
#train_tsv.drop( train_tsv[ train_tsv['cena'] > 5000000 ].index , inplace=True)
#train_tsv.drop( train_tsv[ train_tsv['cena'] < 50000 ].index , inplace=True)
#train_tsv.drop( train_tsv[ train_tsv['Powierzchnia w m2'] > 1000 ].index , inplace=True)

#train_tsv['Piętro'].replace(["parter", " parter"], 0, inplace=True)
train_tsv = train_normalize(train_tsv)
#print (train_tsv.sort_values(by='Powierzchnia w m2', ascending=True))

#counting all diffrents elements print (dev_in_tsv.groupby('Miejsce parkingowe').mean())
#print (dev_in_tsv.groupby('Powierzchnia w m2').mean())
#print (dev_in_tsv.groupby('Liczba pokoi').mean())
#print (dev_in_tsv.groupby('Miejsce parkingowe').mean())
#print (dev_in_tsv.groupby('Piętro').mean())
#print (dev_in_tsv.groupby('Liczba pięter w budynku').mean())


x = train_tsv[['Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku', 'Piętro']]
y = train_tsv['cena']

dev_in_tsv = data_normalize(dev_in_tsv)
test_in_tsv = data_normalize(test_in_tsv)

regresion = LinearRegression()
regresion.fit(x, y)


dev_0 = regresion.predict(dev_in_tsv[['Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku', 'Piętro']])
test_A = regresion.predict(test_in_tsv[['Powierzchnia w m2', 'Liczba pokoi', 'Miejsce parkingowe', 'Liczba pięter w budynku', 'Piętro']])

outF1 = open("dev-0/out.tsv", "w")
for line1 in dev_0:
	outF1.write('%.0f\n' % line1)
outF1.close()

outF2 = open("test-A/out.tsv", "w")
for line2 in test_A:
	outF2.write('%.0f\n' % line2)
outF2.close()


print (time.time() - start_time)



