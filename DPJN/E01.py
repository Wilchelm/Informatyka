import urllib2, re
szlifierki = []
for i in range(39):
    response = urllib2.urlopen("https://www.ceneo.pl/Szlifierki_i_polerki/Rodzaj:Szlifierki_katowe;0020-30-0-0-%d.htm"%i)
    page_source =response.read()
    szlifierki +=re.findall(r'data-source-tag="">([A-Za-z0-9 ]+)</a>', page_source)
print set(szlifierki)



