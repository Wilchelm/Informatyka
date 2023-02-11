#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, csv, numpy, pandas, time

start_time = time.time()

# Hipoteza: funkcja liniowa jednej zmiennej
def h(theta, x):
	return theta[0] + theta[1] * x

def J(h, theta, x, y):
	m = len(y)
	return 1.0 / (2 * m) * sum((h(theta, x[i]) - y[i])**2 for i in range(m))

def costfun(fun, x, y):
	return lambda theta: J(fun, theta, x, y)

def gradient_descent(h, cost_fun, theta, x, y, alpha, eps):
	current_cost = cost_fun(h, theta, x, y)
	log = [[current_cost, theta]]  # log przechowuje wartości kosztu i parametrów
	m = len(y)
	while True:
		new_theta = [theta[0] - alpha/float(m) * sum(h(theta, x[i]) - y[i] for i in range(m)), theta[1] - alpha/float(m) * sum((h(theta, x[i]) - y[i]) * x[i] for i in range(m))]
		theta = new_theta  # jednoczesna aktualizacja - używamy zmiennej tymaczasowej
		try:
			current_cost, prev_cost = cost_fun(h, theta, x, y), current_cost
		except OverflowError:
			break  
		if abs(prev_cost - current_cost) <= eps:
			break     
		log.append([current_cost, theta])
	return theta, log

#def normalize(values):
#	return (values - numpy.mean(values, axis=0)) / (numpy.amax(values, axis=0))

def normalize(values):
	return (values - numpy.mean(values, axis=0)) / (numpy.std(values, axis=0))



train_tsv = pandas.read_csv('train/train.tsv', sep='\t', header=0)
dev_in_tsv = pandas.read_csv('dev-0/in.tsv', sep='\t', header=None,)
test_in_tsv = pandas.read_csv('test-A/in.tsv', sep='\t', header=None)

train_tsv = train_tsv.fillna(0)
dev_in_tsv = dev_in_tsv.fillna(0)
test_in_tsv = test_in_tsv.fillna(0)

x = train_tsv['Powierzchnia w m2']
x = normalize(x)
y = train_tsv['cena']

dev_in_tsv = normalize(dev_in_tsv)
test_in_tsv = normalize(test_in_tsv)

best_theta, log = gradient_descent(h, J, [0.0, 0.0], x, y, alpha=0.05, eps=0.0001)



#print (h(best_theta, dev_in_tsv))
#print (h(best_theta, test_in_tsv))

dev_0 = h(best_theta, dev_in_tsv)
test_A = h(best_theta, test_in_tsv)

outF1 = open("dev-0/out.tsv", "w")
for line1 in dev_0:
	outF1.write('%.0f\n' % line1)
outF1.close()

outF2 = open("test-A/out.tsv", "w")
for line2 in test_A:
	outF2.write('%.0f\n' % line2)
outF2.close()


print (time.time() - start_time)
