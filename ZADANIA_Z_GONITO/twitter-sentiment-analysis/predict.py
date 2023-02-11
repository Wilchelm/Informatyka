#cat test-A/in.tsv | python3 predict.py > test-A/out.tsv
#cat dev-0/in.tsv | python3 predict.py > dev-0/out.tsv
import pickle
import sys
from math import log

model = pickle.load(open("model.p", "rb"))

positives_counts, negatives_counts, positives, negatives, positives_total, negatives_total = model

vocabulary_size = len(set(positives_counts).union(set(negatives_counts)))

positives_logprob_apriori = log(positives / (positives + negatives))
negatives_logprob_apriori = log(negatives / (positives + negatives))

for line in sys.stdin:
	text = line.strip()
	terms = text.split(" ")
	for term in terms:
		term = term.lower()

	positives_logprob = positives_logprob_apriori
	for term in terms:
		term_count = positives_counts[term] if term in positives_counts else 0
		positives_logprob += log((term_count + 1) / (positives_total + vocabulary_size))	

	negatives_logprob = negatives_logprob_apriori
	for term in terms:
		term_count = negatives_counts[term] if term in negatives_counts else 0
		negatives_logprob += log((term_count + 1) / (negatives_total + vocabulary_size))
	
	if positives_logprob > negatives_logprob:
		print ("0.78")
	else:
		print ("0.22")
