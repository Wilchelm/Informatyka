#include <iostream>
#include <string>
using namespace std;

class Pojazd
{
	public:
		virtual float podajWage() {}
		void ustalNazwe(string n) { nazwa = n; }
		const string podajNazwe() { return nazwa;}
	private:
		string nazwa;
};

class Samochod : public Pojazd
{
	public:
		
		 void ustalWage(float w1, float w2) {wagaSilnika = w1; wagaKaroserii = w2; }
		 float podajWage() {return wagaSilnika+wagaKaroserii;};
	private:
		float wagaSilnika;
		float wagaKaroserii;
};

class Motocykl : public Pojazd
{
	public: 
		float podajWage() {};
		int ustalWage(float w){wagaCalkowita = w;	}
	private:
		float wagaCalkowita;	
};

int iloscPojazdow = 0;
Pojazd * tablicaPojazdow[5];

void dodajSamochod(string nazwa, float wagaSilnika, float wagaKaroserii) {
    Samochod * s = new Samochod();
    s->ustalNazwe(nazwa);
    s->ustalWage(wagaSilnika, wagaKaroserii);
        
        tablicaPojazdow[iloscPojazdow++] = s;
}

void dodajMotocykl(string nazwa, float wagaCalkowita) {
    Motocykl * m = new Motocykl();
    m->ustalNazwe(nazwa);
    m->ustalWage(wagaCalkowita);
        
        tablicaPojazdow[iloscPojazdow++] = m;
}

void wypiszDanePojazdow(Pojazd * wskPojazd) {

   cout << wskPojazd->podajNazwe()
            << " "
            << wskPojazd->podajWage()
            << "\n";
}

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
		// wypelnianie tablicy danych        
        dodajSamochod("BMW",1978,1500);
        dodajSamochod("Fiat",1978,1500);
        dodajSamochod("Jeep",1978,1500);
        dodajMotocykl("Yamaha",380);
        dodajMotocykl("Honda",400);

        //wypisanie danych z tablicy osob
        for(int i = 0;i<iloscPojazdow;i++) {
                wypiszDanePojazdow(tablicaPojazdow[i]);
        }
        
     
	return 0;
}
