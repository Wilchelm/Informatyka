# -*- coding: utf-8 -*-
from urllib.request import urlopen
from collections import Counter
from operator import sub
import  re, numpy
kluby = []

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2008/2009)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2009/2010)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2010/2011)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2011/2012)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2012/2013)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2013/2014)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2014/2015)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2015/2016)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

response = urlopen("https://pl.wikipedia.org/wiki/Ekstraklasa_w_pi%C5%82ce_no%C5%BCnej_(2016/2017)")
page_source =response.read().decode('utf-8')
kluby +=re.findall(r'title="[A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ()]*">([A-Za-zżźćńółęąśŻŹĆĄŚĘŁÓŃ._ ]*)<\/a>.*\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td>[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td width="[0-9]*">[0-9]*<\/td>\n<td>[0-9+−]*<\/td>\n<td><b>([0-9]*)', page_source)

kluby = sorted(kluby)
l=len(kluby)
l=l-2
print (kluby)
#for x,y in kluby:
#	print (x)
#	print (y)
#print ("\n\n\n\n\n\n\n")
#z=sorted(kluby, key=lambda x: x[1])[::-1]
#print (z)
