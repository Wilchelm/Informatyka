# -*- coding: utf-8 -*-
from math import sin, cos, sqrt, atan2, radians
from array import array
import time, re, json
from urllib.request import urlopen

def dist(lon1, lat1, lon2, lat2):
	R = 6373.0

	lat1 = radians(lat1)
	lon1 = radians(lon1)
	lat2 = radians(lat2)
	lon2 = radians(lon2)

	dlon = lon2 - lon1
	dlat = lat2 - lat1

	a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
	c = 2 * atan2(sqrt(a), sqrt(1 - a))

	distance = R * c
	return distance

def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

def Found(line):
	x=re.findall(r'\"next_page_token\": \"([A-Za-z0-9-_]*)',line)
	if len(x)>0:
		return True
	else:
		return False
	

def GoogPlac(lat,lng):
	#making the url
	AUTH_KEY = "AIzaSyAyK6k9Cfz73bWgh3EH4wLJCVNLYOu_5ds"
	LOCATION = str(lat) + "," + str(lng)
	RADIUS = "50000"
	TYPES = "gas_station"
	MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
		 '?location=%s'
	  	 '&radius=%s'
	  	 '&types=%s'
	  	 '&key=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY)
	#grabbing the JSON result
	response = urlopen(MyUrl)
	jsonRaw = response.read().decode('utf8')
	response.close()
	jsonData = json.loads(jsonRaw)
	time.sleep(3)
	return jsonData

def GoogPlacNext(lat,lng,token):
	#making the url
	AUTH_KEY = "AIzaSyAyK6k9Cfz73bWgh3EH4wLJCVNLYOu_5ds"
	LOCATION = str(lat) + "," + str(lng)
	RADIUS = "50000"
	TYPES = "gas_station"
	TOKEN = str(token)
	MyUrl = ('https://maps.googleapis.com/maps/api/place/nearbysearch/json'
		 '?location=%s'
	  	 '&radius=%s'
	  	 '&types=%s'
	  	 '&key=%s'
		 '&pagetoken=%s') % (LOCATION, RADIUS, TYPES, AUTH_KEY, TOKEN)
	#grabbing the JSON result
	response = urlopen(MyUrl)
	jsonRaw = response.read().decode('utf8')
	response.close()
	jsonData = json.loads(jsonRaw)
	time.sleep(3)
	return jsonData


frow=input("1-Zbierz dane\n2-Analizuj dane\n\n")
if (frow=="1"):
	l = []
	my_file=open('wspol.txt','r')
	for line in my_file.readlines():
		l.append(line.strip("\n"))

	for line1 in l:
		x,y = line1.split(",")
		x=float(x)
		y=float(y)
		for line2 in l:
			a,b = line2.split(",")
			a = float(a)
			b = float(b)
			km=dist(x,y,a,b)
			if 0<km<50 :
				line2=line2.strip("\n")
				l.remove(line2)
		line1=line1.strip("\n")
		l.remove(line1)	


	frow2=input("\n1-[0-19]\n2-[20-39]\n3-[40-59]\n\n")
	if (frow2=="1"):
		for line in l:
			a,b = line.split(",")
			a = float(a)
			b = float(b)
			print (line)
			with open('D3/'+line+'.txt', 'w') as outfile:
	   			json.dump(GoogPlac(b,a), outfile)
			
	if (frow2=="2"):
		for line in l:
			print (line)
			my_file=open('D3/'+line+'.txt','r')
			for line2 in my_file.readlines():
				if Found(line2)==True:	
					k=re.findall(r'\"next_page_token\": \"([A-Za-z0-9-_]*)',line2)[0]
					with open('D3/'+line+'_1.txt', 'w') as outfile:
			   			json.dump(GoogPlacNext(b,a,k), outfile)

	if (frow2=="3"):
		for line in l:
			print (line)
			my_file2=open('D3/'+line+'_1.txt','r')
			for line2 in my_file2.readlines():
				if Found(line2)==True:	
					k=re.findall(r'\"next_page_token\": \"([A-Za-z0-9-_]*)',line2)[0]
					with open('D3/'+line+'_2.txt', 'w') as outfile:
			   			json.dump(GoogPlacNext(b,a,k), outfile)
					

if (frow=="2"):
	l = []
	my_file=open('wspol.txt','r')
	for line in my_file.readlines():
		l.append(line.strip("\n"))

	for line1 in l:
		x,y = line1.split(",")
		x=float(x)
		y=float(y)
		for line2 in l:
			a,b = line2.split(",")
			a = float(a)
			b = float(b)
			km=dist(x,y,a,b)
			if 0<km<50 :
				line2=line2.strip("\n")
				l.remove(line2)
		line1=line1.strip("\n")
		l.remove(line1)	

	name=[]
	lat=[]
	lng=[]
	vicinity=[]


	for line in l:
		a,b = line.split(",")
		a = float(a)
		b = float(b)
		filee=open('D3/'+line+'.txt', 'r')
		for x in filee.readlines():
			name+=re.findall(r'\"name\": \"([A-Za-z -]*)',x)
			lat+=re.findall(r'\"geometry\": {\"viewport\": {\"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*}}',x)
			lng+=re.findall(r'\"geometry\": {\"viewport\": {\"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)}}',x)

			lat+=re.findall(r'\"geometry\": {\"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*',x)
			lng+=re.findall(r'\"geometry\": {\"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)',x)

			lat+=re.findall(r'\"geometry\": {\"viewport\": {\"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*}}',x)
			lng+=re.findall(r'\"geometry\": {\"viewport\": {\"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)}}',x)
			vicinity+=re.findall(r'\"vicinity\": \"([A-Za-z ,\\0-9-;]*)',x)
	print(len(name),len(lat),len(lng),len(vicinity))

	for line in l:
		a,b = line.split(",")
		a = float(a)
		b = float(b)
		filee=open('D3/'+line+'_1.txt', 'r')
		for x in filee.readlines():
			name+=re.findall(r'\"name\": \"([A-Za-z -]*)',x)
			lat+=re.findall(r'\"geometry\": {\"viewport\": {\"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*}}',x)
			lng+=re.findall(r'\"geometry\": {\"viewport\": {\"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)}}',x)

			lat+=re.findall(r'\"geometry\": {\"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*',x)
			lng+=re.findall(r'\"geometry\": {\"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)',x)

			lat+=re.findall(r'\"geometry\": {\"viewport\": {\"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*}}',x)
			lng+=re.findall(r'\"geometry\": {\"viewport\": {\"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)}}',x)
			vicinity+=re.findall(r'\"vicinity\": \"([A-Za-z ,\\0-9-;]*)',x)
	print(len(name),len(lat),len(lng),len(vicinity))
	for line in l:
		a,b = line.split(",")
		a = float(a)
		b = float(b)
		filee=open('D3/'+line+'_2.txt', 'r')
		for x in filee.readlines():
			name+=re.findall(r'\"name\": \"([A-Za-z -]*)',x)
			lat+=re.findall(r'\"geometry\": {\"viewport\": {\"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*}}',x)
			lng+=re.findall(r'\"geometry\": {\"viewport\": {\"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)}}',x)

			lat+=re.findall(r'\"geometry\": {\"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*',x)
			lng+=re.findall(r'\"geometry\": {\"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)',x)

			lat+=re.findall(r'\"geometry\": {\"viewport\": {\"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": ([0-9.]*), \"lng\": [0-9.]*}}',x)
			lng+=re.findall(r'\"geometry\": {\"viewport\": {\"southwest\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}, \"northeast\": {\"lat\": [0-9.]*, \"lng\": [0-9.]*}}, \"location\": {\"lat\": [0-9.]*, \"lng\": ([0-9.]*)}}',x)
			vicinity+=re.findall(r'\"vicinity\": \"([A-Za-z ,\\0-9-;]*)',x)
	print(len(name),len(lat),len(lng),len(vicinity))

	dlugosc=len(name)
	zmienna=0
	fuels=open('fuels2.txt','w')
	while zmienna<dlugosc:
		
		linia= "new Models.Fuels\n{\nStation = \"" + name[zmienna] + "\",\nAddress = \"" + vicinity[zmienna] + "\",\nLatitude = " + lat[zmienna] + ",\nLongitude = " + lng[zmienna] + ",\nPetrol95 = new List <Petrol95> (),\nPetrol98 = new List <Petrol98> (),\nDiesel = new List <Diesel> (),\nLPG = new List <LPG> ()\n},\n" 
		fuels.write(linia)
		zmienna+=1







		
