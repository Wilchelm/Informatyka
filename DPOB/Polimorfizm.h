#ifndef Polimorfizm_H
#define Polimorfizm_H

#include <string>
#include <iostream>
class Osoba
{
 public:
 	
  virtual float wydatekOsobowy() {}

  void ustalImie(string i) { imie = i; }
  void ustalNazwisko(string n) { nazwisko = n; }
  void ustalRokUr(int r) { rokur=r; }

  const string podajImie() { return imie; }
  const string podajNazwisko() { return nazwisko; }
  int podajRokUr() { return rokur; }

  void ustalDane(string i, string n, int r);

  Osoba() {};
  Osoba(string i, string n, int r);

 private:
  string imie;
  string nazwisko;
  int rokur;
  
};

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

class Student : public Osoba
{
	private:
		int stypendium;
	public:
		int podajStypendium()
		{
			return stypendium;
		}
		
		void ustalStypendium(double st)
		{
			stypendium = st;
		}
		float wydatekOsobowy();
};

float Student::wydatekOsobowy() {
	return stypendium;
}

class Pracownik : public Osoba
{
	private:
		int pensja;
	public:
		float wydatekOsobowy();
		void ustalPensje (double p)
		{
			pensja = p;
		}
		int podajPensje ()
		{
			return pensja;
		}
		int podajPremie()
		{
			return 0.2*pensja;
		}
};

float Pracownik::wydatekOsobowy() {
	return podajPensje() + podajPremie();
}

#endif
