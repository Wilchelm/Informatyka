# -*- coding: utf-8 -*-
import urllib.request, sys, re, os


def remove_general_ends(word):
    if len(word) > 4 and word[-2:] in {"ia", "ie"}:
        return word[:-2]
    if len(word) > 4 and word[-1:] in {"u", u"ą", "i", "a", u"ę", "y", u"ę", u"ł"}:
        return word[:-1]
    return word
    
def remove_diminutive(word):
    if len(word) > 6:
        if word[-5:] in {"eczek", "iczek", "iszek", "aszek", "uszek"}:
            return word[:-5]
        if word[-4:] in {"enek", "ejek", "erek"}:
            return word[:-2]
    if len(word) > 4:
        if word[-2:] in {"ek", "ak"}:
            return word[:-2]
    return word
    
def remove_verbs_ends(word):
    if len(word) > 5 and word.endswith("bym"):
        return word[:-3]
    if len(word) > 5 and word[-3:] in {"esz", "asz", "cie", u"eść", u"aść", u"łem", u"łam", "amy", "emy"}:
        return word[:-3]
    if len(word) > 3 and word[-3:] in {"esz", "asz", u"eść", u"aść", u"eć", u"ać"}:
        return word[:-2]
    if len(word) > 3 and word[-3:] in {"aj"}:
        return word[:-1]
    if len(word) > 3 and word[-2:] in {u"ać", "em", "am", u"ał", u"ił", u"ić", u"ąc"}:
        return word[:-2]
    return word

def remove_nouns(word):
    if len(word) > 7 and word[-5:] in {"zacja", u"zacją", "zacji"}:
        return word[:-4]
    if len(word) > 6 and word[-4:] in {"acja", "acji", u"acją", "tach", "anie", "enie",
    "eniu", "aniu"}:
        return word[:-4]
    if len(word) > 6 and word.endswith("tyka"):
        return word[:-2]
    if len(word) > 5 and word[-3:] in {"ach", "ami", "nia", "niu", "cia", "ciu"}:
        return word[:-3]
    if len(word) > 5 and word[-3:] in {"cji", "cja", u"cją"}:
        return word[:-2]
    if len(word) > 5 and word[-2:] in {"ce", "ta"}:
        return word[:-2]
    return word
    
def remove_adjective_ends(word):
    if len(word) > 7 and word.startswith("naj") and (word.endswith("sze")
    or word.endswith("szy")):
        return word[3:-3]
    if len(word) > 7 and word.startswith("naj") and word.endswith("szych"):
        return word[3:-5]
    if len(word) > 6 and word.endswith("czny"):
        return word[:-4]
    if len(word) > 5 and word[-3:] in {"owy", "owa", "owe", "ych", "ego"}:
        return word[:-3]
    if len(word) > 5 and word[-2:] in {"ej"}:
        return word[:-2]
    return word
    
def remove_adverbs_ends(word):
    if len(word) > 4 and word[:-3] in {"nie", "wie"}:
        return word[:-2]
    if len(word) > 4 and word.endswith("rze"):
        return word[:-2]
    return word

def remove_plural_forms(word):
    if len(word) > 4 and (word.endswith(u"ów") or word.endswith("om")):
        return word[:-2]
    if len(word) > 4 and word.endswith("ami"):
        return word[:-3]
    return word
    
'''
l=[]
my_dir = os.path.expanduser('~/Pobrane/sjp-odm-20171208/wyrazy.txt')
f=open(my_dir,'r')
for line in f.readlines():
	l.append(line.strip("\n"))
l=set(l)
'''

pomocnicza = input("1-zbierz dane 2- program 3-zakończ program\n")

###################################################################################

if pomocnicza == '1':

	#################################################
	################RZECZOWNIKI######################
	#################################################

	rzeczowniki = []
	rzeczowniki_link = []


	response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_rzeczowniki&pagefrom=a#mw-pages")
	page_source =response.read().decode('utf-8')
	rzeczowniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
	rzeczowniki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
	print (len(rzeczowniki))

	i=0
	while i<254:
		response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_rzeczowniki&pagefrom="+rzeczowniki_link[-1]+"#mw-pages")
		page_source =response.read().decode('utf-8')
		rzeczowniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
		rzeczowniki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
		i+=1
		print (i)
		print (len(rzeczowniki))
	rzeczowniki=set(rzeczowniki)

	f1=open('rzeczowniki.txt', 'w')
	for x in rzeczowniki:
		f1.write(x+"\n")

	#################################################
	##################SPÓJNIKI#######################
	#################################################

	spojniki=[]

	response = urllib.request.urlopen("https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_polski_-_sp%C3%B3jniki")
	page_source =response.read().decode('utf-8')
	spojniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)

	print (len(spojniki))

	f2=open('spojniki.txt', 'w')
	for x in spojniki:
		f2.write(x+"\n")

	#################################################
	####################ZAIMKI#######################
	#################################################

	zaimki = []

	response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_zaimki&pagefrom=a#mw-pages")
	page_source =response.read().decode('utf-8')
	zaimki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)

	response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_zaimki&pagefrom=iluoki#mw-pages")
	page_source =response.read().decode('utf-8')
	zaimki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)

	response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_zaimki&pagefrom=tw%C3%B3j#mw-pages")
	page_source =response.read().decode('utf-8')
	zaimki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)

	print (len(zaimki))

	f3=open('zaimki.txt', 'w')
	for x in zaimki:
		f3.write(x+"\n")


	#################################################
	#################PRZYSŁÓWKI######################
	#################################################

	przyslowki = []
	przyslowki_link = []


	response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_przys%C5%82%C3%B3wki&pagefrom=a#mw-pages")
	page_source =response.read().decode('utf-8')
	przyslowki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
	przyslowki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
	print (len(przyslowki))

	i=0
	while i<12:
		response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_przys%C5%82%C3%B3wki&pagefrom="+przyslowki_link[-1]+"#mw-pages")
		page_source =response.read().decode('utf-8')
		przyslowki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
		przyslowki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
		i+=1
		print (i)
		print (len(przyslowki))
	przyslowki=set(przyslowki)

	f4=open('przyslowki.txt', 'w')
	for x in przyslowki:
		f4.write(x+"\n")


	#################################################
	#################PRZYMIOTNIKI####################
	#################################################

	przymiotniki = []
	przymiotniki_link = []


	response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_przymiotniki&pagefrom=a#mw-pages")
	page_source =response.read().decode('utf-8')
	przymiotniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
	przymiotniki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
	print (len(przymiotniki))

	i=0
	while i<57:
		response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_przymiotniki&pagefrom="+przymiotniki_link[-1]+"#mw-pages")
		page_source =response.read().decode('utf-8')
		przymiotniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
		przymiotniki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
		i+=1
		print (i)
		print (len(przymiotniki))
	przymiotniki=set(przymiotniki)

	f5=open('przymiotniki.txt', 'w')
	for x in przymiotniki:
		f5.write(x+"\n")


	#################################################
	##################PRZYIMKI#######################
	#################################################

	przyimki = []

	response = urllib.request.urlopen("https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_polski_-_przyimki")
	page_source =response.read().decode('utf-8')
	przyimki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)


	print (len(przyimki))

	f6=open('przyimki.txt', 'w')
	for x in przyimki:
		f6.write(x+"\n")

	#################################################
	#################PARTYKÓŁY#######################
	#################################################

	partykoly = []

	response = urllib.request.urlopen("https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_polski_-_partyku%C5%82y")
	page_source =response.read().decode('utf-8')
	partykoly +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)


	print (len(partykoly))

	f7=open('partykoly.txt', 'w')
	for x in partykoly:
		f7.write(x+"\n")

	#################################################
	#################LICZEBNIKI######################
	#################################################

	liczebniki = []

	response = urllib.request.urlopen("https://pl.wiktionary.org/wiki/Kategoria:J%C4%99zyk_polski_-_liczebniki")
	page_source =response.read().decode('utf-8')
	liczebniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)


	print (len(liczebniki))

	f8=open('liczebniki.txt', 'w')
	for x in liczebniki:
		f8.write(x+"\n")


	#################################################
	#################CZASOWNIKI######################
	#################################################

	czasowniki = []
	czasowniki_link = []


	response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_czasowniki&pagefrom=a#mw-pages")
	page_source =response.read().decode('utf-8')
	czasowniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
	czasowniki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
	print (len(czasowniki))

	i=0
	while i<34:
		response = urllib.request.urlopen("https://pl.wiktionary.org/w/index.php?title=Kategoria:J%C4%99zyk_polski_-_czasowniki&pagefrom="+czasowniki_link[-1]+"#mw-pages")
		page_source =response.read().decode('utf-8')
		czasowniki +=re.findall(r'[#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)<\/a>', page_source)
		czasowniki_link += re.findall(r'([#%0-9A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*)\" title=\"[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*\">[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ-]*<\/a>', page_source)
		i+=1
		print (i)
		print (len(czasowniki))
	czasowniki=set(czasowniki)

	f9=open('czasowniki.txt', 'w')
	for x in czasowniki:
		f9.write(x+"\n")

###################################################################################

if pomocnicza == '2':

	l = []
	rzeczowniki = []
	spojniki = []
	zaimki = []
	przyslowki = []
	przymiotniki = []
	przyimki = []
	partykoly = []
	liczebniki = []
	czasowniki = []

	znaleźć = [u"znaleźć", u"znajdę", "znajdziesz", "znajdzie", "znajdziemy", "znajdziecie", u"znajdą", u"znalazłem", u"znalazłeś", u"znalazł", u"znaleźliśmy", "znaleźliście", u"znaleźli", u"znalazłam", u"znalazłaś", u"znalazła", u"znalazłyśmy", u"znalazłyście", u"znalazły", u"znalazłom", u"znalazłoś", u"znalazło", u"znajdę", u"znajdź", "znajdzie", u"znajdźmy", u"znajdźcie", u"znajdą"]

	brać = [u"brać", u"biorę", "bierzesz", "bierze", "bierzemy", "bierzecie", u"biorą"," brałem", u"brałeś", u"brał", u"braliśmy", u"braliście", "brali", u"brałam", u"brałaś", u"brała", u"brałyśmy", u"brałyście", u"brały", u"brałom", u"brałoś", u"brało", u"biorę", "bierz", "bierze", "bierzmy", "bierzcie", u"biorą"]

	być = [u"być", "jestem", u"jesteś", "jest", u"jesteśmy", u"jesteście", u"są", u"byłem", u"byłeś", u"był", u"byliśmy", u"byliście", "byli", u"byłam", u"byłaś", u"była", u"byłyśmy", u"byłyście", u"były", u"byłom", u"byłoś", u"było", u"będę", u"bądź", u"będzie", u"bądźmy", u"bądźcie", u"będą"]

	ciąć = [u"ciąć", u"tnę", "tniesz", "tnie", "tniemy", "tniecie", u"tną", u"ciąłem", u"ciąłeś", u"ciął", u"cięliśmy", u"cięliście", u"cięli", u"cięłam", u"cięłaś", u"cięła", u"cięłyśmy", u"cięłyście", u"cięły", u"cięłom", u"cięłoś", u"cięło", u"tnę", "tnij", "tnie", "tnijmy", "tnijcie", u"tną"]

	dojść = [u"dojść", u"dojdę", "dojdziesz", "dojdzie", "dojdziemy", "dojdziecie", u"dojdą", u"doszedłem", u"doszedłeś", u"doszedł", u"doszliśmy", u"doszliście", "doszli", u"doszłam", u"doszłaś", u"doszła", u"doszłyśmy", u"doszłyście", u"doszły", u"doszłom", u"doszłoś", u"doszło", u"dojdę", u"dojdź", "dojdzie", u"dojdźmy", u"dojdźcie", u"dojdą"]

	gnieść = [u"gnieść", u"gniotę", "gnieciesz", "gniecie", "gnieciemy", "gnieciecie", u"gniotą", u"gniotłem", u"gniotłeś", u"gniótł", u"gnietliśmy", u"gnietliście", "gnietli", u"gniotłam", u"gniotłaś", u"gniotła", u"gniotłyśmy", u"gniotłyście", u"gniotły", u"gniotłom", u"gniotłoś", u"gniotło", u"gniotę", u"gnieć", "gniecie", u"gniećmy", u"gniećcie", u"gniotą"]

	iść = [u"iść", u"idę", "idziesz", "idzie", "idziemy", "idziecie", u"idą", u"szedłem", u"szedłeś", u"szedł", u"szliśmy", u"szliście", "szli", u"szłam", u"szłaś", u"szła", u"szłyśmy", u"szłyście", u"szły", u"szłom", u"szłoś", u"szło", u"idę", u"idź", "idzie", u"idźmy", u"idźcie", u"idą"]

	jeść = [u"jeść", "jem", "jesz", "je", "jemy", "jecie", u"jedzą", u"jadłem", u"jadłeś", u"jadł", u"jedliśmy", u"jedliście", "jedli", u"jadłam", u"jadłaś", u"jadła", u"jadłyśmy", u"jadłyście", u"jadły", u"jadłom", u"jadłoś", u"jadło", "jem", "jedz", "je", "jedzmy", "jedzcie", u"jedzą"]

	mieć = [u"mieć", "mam", "masz", "ma", "mamy", "macie", u"mają", u"miałem", u"miałeś", u"miał", u"mieliśmy", u"mieliście", "mieli", u"miałam", u"miałaś", u"miała", u"miałyśmy", u"miałyście", u"miały", u"miałom", u"miałoś", u"miało", "mam", "miej", "ma", "miejmy", "miejcie", u"mają"]

	móc = [u"móc", u"mogę", u"możesz", u"może", u"możemy", u"możecie", u"mogą", u"mogłem", u"mogłeś", u"mógł", u"mogliśmy", u"mogliście", "mogli", u"mogłam", u"mogłaś", u"mogła", u"mogłyśmy", u"mogłyście", u"mogły", u"mogłom", u"mogłoś", u"mogło"]

	nieść = [u"nieść", u"niosę", "niesiesz", "niesie", "niesiemy", "niesiecie", u"niosą", u"niosłem", u"niosłeś", u"niósł", u"nieśliśmy", u"nieśliście", u"nieśli", u"niosłam", u"niosłaś", u"niosła", u"niosłyśmy", u"niosłyście", u"niosły", u"niosłom", u"niosłoś", u"niosło", u"niosę", u"nieś", "niesie", u"nieśmy", u"nieście", u"niosą"]

	pachnieć = [u"pachnieć", u"pachnę", "pachniesz", "pachnie", "pachniemy", "pachniecie", u"pachną", u"pachnąłem", u"pachnąłeś", u"pachniał", u"pachnieliśmy", u"pachnieliście", "pachnieli", u"pachniałam", u"pachniałaś", u"pachniała", u"pachniałyśmy", u"pachniałyście", u"pachniały", u"pachniałom", u"pachniałoś", u"pachniało", u"pachnę", "pachnij", "pachnie", "pachnijmy", "pachnijcie", u"pachną"]

	pomóc = [u"pomóc", u"pomogę", u"pomożesz", u"pomoże", u"pomożemy", u"pomożecie", u"pomogą", u"pomogłem", u"pomogłeś", u"pomógł", u"pomogliśmy", u"pomogliście", "pomogli", u"pomogłam", u"pomogłaś", u"pomogła", u"pomogłyśmy", u"pomogłyście", u"pomogły", u"pomogłom", u"pomogłoś", u"pomogło", u"pomogę", u"pomóż", u"pomoże", u"pomóżmy", u"pomóżcie", u"pomogą"]

	spiąć = [u"spiąć", u"zepnę", "zepniesz", "zepnie", "zepniemy", "zepniecie", u"zepną", u"spiąłem", u"spiąłeś", u"spiął", u"spięliśmy", u"spięliście", u"spięli", u"spięłam", u"spięłaś", u"spięła", u"spięłyśmy", u"spięłyście", u"spięły", u"spięłom", u"spięłoś", u"spięło", u"zepnę", "zepnij", "zepnie", "zepnijmy", "zepnijcie", u"zepną"]

	siąść = [u"siąść", u"siądę", u"siądziesz", u"siądzie", u"siądziemy", u"siądziecie", u"siądą", u"siadłem", u"siadłeś", u"siadł", u"siedliśmy", u"siedliście", "siedli", u"siadłam", u"siadłaś", u"siadła", u"siadłyśmy", u"siadłyście", u"siadły", u"siadłom", u"siadłoś", u"siadło", u"siądę", u"siądź", u"siądzie", u"siądźmy", u"siądźcie", u"siądą"]

	trzeć = [u"trzeć", u"trę", "trzesz", "trze", "trzemy", "trzecie", u"trą", u"tarłem", u"tarłeś", u"tarł", u"tarliśmy", u"tarliście", "tarli", u"tarłam", u"tarłaś", u"tarła", u"tarłyśmy", u"tarłyście", u"tarły", u"tarłom", u"tarłoś", u"tarło", u"trę", "trzyj", "trze", "trzyjmy", "trzyjcie", u"trą"]

	usiąść = [u"usiąść", u"usiądę", u"usiądziesz", u"usiądzie", u"usiądziemy", u"usiądziecie", u"usiądą", u"usiadłem", u"usiadłeś", u"usiadł", u"usiedliśmy", u"usiedliście", "usiedli", u"usiadłam", u"usiadłaś", u"usiadła", u"usiadłyśmy", u"usiadłyście", u"usiadły", u"usiadłom", u"usiadłoś", u"usiadło", u"usiądę", u"usiądź", u"usiądzie", u"usiądźmy", u"usiądźcie", u"usiądą"]

	wejść = [u"wejść", u"wejdę", "wejdziesz", "wejdzie", "wejdziemy", "wejdziecie", u"wejdą", u"wszedłem", u"wszedłeś", u"wszedł", u"weszliśmy", u"weszliście", "weszli", u"weszłam", u"weszłaś", u"weszła", u"weszłyśmy", u"weszłyście", u"weszły", u"weszłom", u"weszłoś", u"weszło", u"wejdę", u"wejdź", "wejdzie", u"wejdźmy", u"wejdźcie", u"wejdą"]

	wiedzieć = [u"wiedzieć", "wiem", "wiesz", "wie", "wiemy",u"wiecie", u"wiedzą", u"wiedziałem", u"wiedziałeś", u"wiedział", u"wiedzieliśmy", u"wiedzieliście", "wiedzieli", u"wiedziałam", u"wiedziałaś", u"wiedziała", u"wiedziałyśmy", u"wiedziałyście", u"wiedziały", u"wiedziałom", u"wiedziałoś", u"wiedziało", "wiem", "wiedz", "wie", "wiedzmy", "wiedzcie", u"wiedzą"]

	wziąć = [u"wziąć", u"wezmę", u"weźmiesz", u"weźmie", u"weźmiemy", u"weźmiecie", u"wezmą", u"wziąłem", u"wziąłeś", u"wziął", u"wzięliśmy", u"wzięliście", u"wzięli", u"wzięłam", u"wzięłaś", u"wzięła", u"wzięłyśmy", u"wzięłyście", u"wzięły", u"wzięłom", u"wzięłoś", u"wzięło", u"wezmę", u"weź", u"weźmij", u"weźmie", u"weźmy", u"weźmijmy", u"weźcie", u"weźmijcie", u"wezmą"]

	zebrać = [u"zebrać", u"zbiorę", "zbierzesz", "zbierze", "zbierzemy", "zbierzecie", u"zbiorą", u"zebrałem", u"zebrałeś", u"zebrał", u"zebraliśmy", u"zebraliście", "zebrali", u"zebrałam", u"zebrałaś", u"zebrała", u"zebrałyśmy", u"zebrałyście", u"zebrały", u"zebrałom", u"zebrałoś", u"zebrało", u"zbiorę", "zbierz", "zbierze", "zbierzmy", "zbierzcie", u"zbiorą"]


	try:
		f1=open('rzeczowniki.txt', 'r')
		for line in f1.readlines():
			rzeczowniki.append(line.strip("\n"))

		f2=open('spojniki.txt', 'r')
		for line in f2.readlines():
			spojniki.append(line.strip("\n"))

		f3=open('zaimki.txt', 'r')
		for line in f3.readlines():
			zaimki.append(line.strip("\n"))

		f4=open('przyslowki.txt', 'r')
		for line in f4.readlines():
			przyslowki.append(line.strip("\n"))

		f5=open('przymiotniki.txt', 'r')
		for line in f5.readlines():
			przymiotniki.append(line.strip("\n"))

		f6=open('przyimki.txt', 'r')
		for line in f6.readlines():
			przyimki.append(line.strip("\n"))

		f7=open('partykoly.txt', 'r')
		for line in f7.readlines():
			partykoly.append(line.strip("\n"))

		f8=open('liczebniki.txt', 'r')
		for line in f8.readlines():
			liczebniki.append(line.strip("\n"))

		f9=open('czasowniki.txt', 'r')
		for line in f9.readlines():
			czasowniki.append(line.strip("\n"))

		l.extend(rzeczowniki)
		l.extend(spojniki)
		l.extend(zaimki)
		l.extend(przyslowki)
		l.extend(przymiotniki)
		l.extend(przyimki)
		l.extend(partykoly)
		l.extend(liczebniki)
		l.extend(czasowniki)

		l=set(l)
		l=sorted(l)

		print ('write quit to end program')

		for line in sys.stdin:
			print ('')
			if line == 'quit\n':
				break
			else:
				for word in line.split():
					zmienna = 1
					regex = re.compile(word)
					if list(filter(regex.match, pachnieć)):
						print ('pachnieć')
						zmienna = 2
					if list(filter(regex.match, nieść)):
						print ('nieść')
						zmienna = 2
					if list(filter(regex.match, móc)):
						print ('móc')
						zmienna = 2
					if list(filter(regex.match, mieć)):
						print ('mieć')
						zmienna = 2
					if list(filter(regex.match, jeść)):
						print ('jeść')
						zmienna = 2
					if list(filter(regex.match, iść)):
						print ('iść')
						zmienna = 2
					if list(filter(regex.match, gnieść)):
						print ('gnieść')
						zmienna = 2
					if list(filter(regex.match, dojść)):
						print ('dojść')
						zmienna = 2
					if list(filter(regex.match, ciąć)):
						print ('ciąć')
						zmienna = 2
					if list(filter(regex.match, być)):
						print ('być')
						zmienna = 2
					if list(filter(regex.match, brać)):
						print ('brać')
						zmienna = 2
					if list(filter(regex.match, pomóc)):
						print ('pomóc')
						zmienna = 2
					if list(filter(regex.match, spiąć)):
						print ('spiąć')
						zmienna = 2
					if list(filter(regex.match, siąść)):
						print ('siąść')
						zmienna = 2
					if list(filter(regex.match, trzeć)):
						print ('trzeć')
						zmienna = 2
					if list(filter(regex.match, usiąść)):
						print ('usiąść')
						zmienna = 2
					if list(filter(regex.match, wejść)):
						print ('wejść')
						zmienna = 2
					if list(filter(regex.match, wiedzieć)):
						print ('wiedzieć')
						zmienna = 2
					if list(filter(regex.match, wziąć)):
						print ('wziąć')
						zmienna = 2
					if list(filter(regex.match, zebrać)):
						print ('zebrać')
						zmienna = 2
					if list(filter(regex.match,znaleźć)):
						print ('znaleźć')
						zmienna = 2
					if zmienna == 1:
						stem = word[:]
						stem = remove_nouns(stem)
						stem = remove_diminutive(stem)
						stem = remove_adjective_ends(stem)
						stem = remove_verbs_ends(stem)
						stem = remove_adverbs_ends(stem)
						stem = remove_plural_forms(stem)
						stem = remove_general_ends(stem)
						regex2=re.compile("^"+stem+".*")
						try:
							x = [m.group(0) for l2 in l for m in [regex2.search(l2)] if m]
							try:
								print (min(x, key=len))
							except ValueError:
								print (stem)	
						except IndexError:
							print (stem)

	except FileNotFoundError:
		print ('Musisz najpierw pobrac dane')


###################################################################################

if pomocnicza == '3':
	print ('')				


