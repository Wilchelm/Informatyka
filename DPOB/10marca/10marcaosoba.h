#ifndef 10MARCAOSOBA_h
#define 10MARCAOSOBA_H

#include <string>
using namespace std;

class Osoba {
private:
	string imie;
	string nazwisko;
	Adres * adres;
public:

	void ustalImie(string i) { imie = i; }
  	void ustalNazwisko(string n) { nazwisko = n; }
	
	void ustalDane(string i, string n);
	void ustalAdres(string i, string n);
	string podajDane(return imie, nawzisko);
	string podajAdres() {return adres};



Osoba::~Osoba()
	{
	delete adres;
	}

};

#endif
