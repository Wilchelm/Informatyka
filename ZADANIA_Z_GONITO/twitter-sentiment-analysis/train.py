# zcat ./train/train.tsv.gz | python3 train.py
import sys
import pickle

positives_counts = {}
negatives_counts = {}
positives = 0
negatives = 0
positives_total = 0
negatives_total = 0

for line in sys.stdin:
	line = line.strip()
	klasa, tekst = line.split('\t')
	terms = tekst.split(' ')
	for term in terms:
		term = term.lower()
	if klasa == '1':
		positives_total += len(terms) 
		positives += 1
		for term in terms:
			if term in positives_counts:
				positives_counts[term] += 1
			else:
				positives_counts[term] = 1
	else:
		negatives_total += len(terms) 
		negatives += 1
		for term in terms:
			if term in negatives_counts:
				negatives_counts[term] += 1
			else:
				negatives_counts[term] = 1

pickle.dump((positives_counts, negatives_counts, positives, negatives, positives_total, negatives_total), open("model.p","wb"))





