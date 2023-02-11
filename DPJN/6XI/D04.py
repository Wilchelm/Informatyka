import re, nltk

f=open("pantadeusz.txt", 'r')
text = f.read().lower()
f.close()
text=re.sub(r'[«»,.\/;:!-?—]', '', text)

tokens = nltk.word_tokenize(text)

print (nltk.FreqDist(tokens).most_common(50))
