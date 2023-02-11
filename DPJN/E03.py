import bs4 as bs
import urllib.request
import os

my_dir = os.path.expanduser('source_pl.txt')
os.remove(my_dir)
f = open(my_dir , 'a')
my_dir2 = os.path.expanduser('source_en.txt')
os.remove(my_dir2)
f2 = open(my_dir2 , 'a')



source_pl = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/index.php').read()
soup_pl = bs.BeautifulSoup(source_pl, 'lxml')

for paragraph in soup_pl.find_all('p'):
	f.write(paragraph.text)

source_pl = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/science.php').read()
soup_pl = bs.BeautifulSoup(source_pl, 'lxml')

for paragraph in soup_pl.find_all('p'):
	f.write(paragraph.text)

source_pl = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/education.php').read()
soup_pl = bs.BeautifulSoup(source_pl, 'lxml')
for paragraph in soup_pl.find_all('p'):
	f.write(paragraph.text)

source_pl = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/relax.php').read()
soup_pl = bs.BeautifulSoup(source_pl, 'lxml')
for paragraph in soup_pl.find_all('p'):
	f.write(paragraph.text)

source_pl = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/contact.php').read()
soup_pl = bs.BeautifulSoup(source_pl, 'lxml')

for paragraph in soup_pl.find_all('p'):
	f.write(paragraph.text)






source_en = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/index_en.php').read()
soup_en = bs.BeautifulSoup(source_en, 'lxml')

for paragraph in soup_en.find_all('p'):
	f2.write(paragraph.text)

source_en = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/science_en.php').read()
soup_en = bs.BeautifulSoup(source_en, 'lxml')

for paragraph in soup_en.find_all('p'):
	f2.write(paragraph.text)

source_en = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/education_en.php').read()
soup_en = bs.BeautifulSoup(source_en, 'lxml')

for paragraph in soup_en.find_all('p'):
	f2.write(paragraph.text)

source_en = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/relax_en.php').read()
soup_en = bs.BeautifulSoup(source_en, 'lxml')

for paragraph in soup_en.find_all('p'):
	f2.write(paragraph.text)

source_en = urllib.request.urlopen('http://www.staff.amu.edu.pl/~rjawor/contact_en.php').read()
soup_en = bs.BeautifulSoup(source_en, 'lxml')

for paragraph in soup_en.find_all('p'):
	f2.write(paragraph.text)

#https://github.com/PorthTechnolegauIaith/alinio


command = 'python alinio.py -e source_pl.txt -c source_en.txt wynik.txt'
os.system(command)

my_dir3 = os.path.expanduser('wynik.txt')

f3 = open(my_dir3, 'r')
while f3.readline():
	print(f3.readline())

