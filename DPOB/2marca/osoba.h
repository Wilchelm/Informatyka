#ifndef OSOBA_H
#define OSOBA_H

#include <string>
using namespace std;
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

#endif
