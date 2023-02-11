#include <string>
#include <iostream>
#include "osoba.h"
#include "student.h"
#include "pracownik.h"

using namespace std;


void Osoba::ustalDane(string i, string n, int r)
{
  ustalImie(i);
  ustalNazwisko(n);
  ustalRokUr(r);
}


Osoba::Osoba(string i, string n, int r)
{
  ustalDane(i,n,r);
}


float Student::wydatekOsobowy() {
	return stypendium;
}

float Pracownik::wydatekOsobowy() {
	return podajPensje() + podajPremie();
}

int main() {

	Student * s = new Student();
	s->ustalDane("Zygfryd","Jelonko", 1995);
	s->ustalStypendium(250);
	Pracownik * p= new Pracownik();
	p->ustalDane("Michal","Nowak",1970);
	p->ustalPensje(1870);
	cout << p->podajPensje() << endl;
	cout << s->podajStypendium() << endl;
	cout << s->wydatekOsobowy() << endl;
	delete s;
	delete p; 
    return 0;
}



