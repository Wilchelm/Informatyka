import re
import bs4 as bs
import urllib.request

def main(adress):
	try:
		sauce = urllib.request.urlopen(adress).read()
		
		# Create a BeautifulSoup object
		soup = bs.BeautifulSoup(sauce,'html.parser')
		
		# Get Unicode
		unicode_str = sauce.decode("utf8")
		# Get a bytestring
		encoded_str = unicode_str.encode("utf8", 'ignore')
		# Create a encoded BeautifulSoup object
		news_soup = bs.BeautifulSoup(encoded_str, "html.parser")
		
	
		# Delete all script and style elements
		for script in soup(["script", "style"]):
			script.decompose() 
	
		text=soup.get_text()
	
		lines = []
		for line in text.splitlines():
			lines.append(line.strip())
		# Delete '' in list
		lines = filter(None, lines)
		text = "\n"
		for i in lines:
			text += i + '\n'
		text = text.replace(",\n",", ")
		#print (text)
		# Find all sentence
		pattern = re.compile(r'[AĄBCĆDEĘFGHIJKLŁMNŃOÓPRSŚTUWYXVZŹŻ][aąbcćdeęfghijklłmnńoóprsśtuwyxvzźż]+[AaĄąBbCcĆćDdEeĘęFfGgHhIiJjKkLlŁłMmNnŃńOoÓóPpRrSsŚśTtUuWwYyZzŹźŻż ,]+[\.!?]')
		rezult = pattern.findall(text)
		
		for i in rezult:
			print(i)
		
		adress = input("Prosze podac adress www ")
		main(adress)
	except:
		adress = input("\n\nWprowadziles zly adress!!!!\nAdres musi miec http lub https\n\nProsze podac adress www ")
		main(adress)

print ('Przyklad onet.pl')
main('https://onet.pl')



