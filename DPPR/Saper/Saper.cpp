#include <iostream>
#include <string>
#include <ctime>
#include <fstream> 
#include "Color.h"
#include "system.h"
#include "Saper.h"
#include "f_getch.h"

using namespace std;

int main()
{
	menu_glowne();
	return 0;
}
void clear_screen() { // czyscimy ekran i pozostawiamy tylko linie z tlumaczeniem sterowania

	clear_screen2();

	cout << "Strzalki - sterowanie w menu gry i po planszyn" << endl; // 75-lewo 77-prawo 72-gora 80-dol

	cout << "Spacja- odslon pole,        " << endl;

	cout << "ESC- wyjscie do menu" << endl;

	cout << "F- flaga,  " << endl;
	
	cout << "V- ?" << endl;

	cout << char(42) << " - mina" << endl;

	cout << char(219) << " - zasloniete pole,         " << endl;

	cout << char(176) << " - odsloniete puste polen" << endl;

	cout << char(83) << " lub " << char(115) << " by zapisac" << endl << endl;

}
void menu_glowne(int i)
{
	
	clear_screen();
	char nawigacja;
	cout << "MENU: Wybierz pozycje za pomoca strzalek i entera" << endl << endl << "NOWA GRA ";

	if (i == 0) {
		
		cout << red << " <-- " << reset;
		
		}
	cout << "WCZYTAJ GRE ";

	if (i == 1) {
		
		cout << red << " <-- " << reset;
		
	}

	cout << "WYJSCIE ";

	if (i == 2) {
		
		cout << red << " <-- " << reset;
		
	}
	else {
		cout << endl; // przesuwa znak zachety ponizej menu, by bylo estetycznie
	}
	do {

		nawigacja = _getch(); // pobiera znak tak dlugo az zostana wcisniete strzalki gora/dol lub enter

	} while (nawigacja != 80 && nawigacja != 72 && nawigacja != 13);

	if (nawigacja == 80) { // w dol

		if (i >= 2) {

			i = 0;
		}
		else {

			i++;
		}

		menu_glowne(i);

	}
	else if (nawigacja == 72) { // w gore

		if (i <= 0) {

			i = 2;
		}
		else {

			i--;
		}

		menu_glowne(i);

	}
	else if (nawigacja == 13) { //enter

		if (i != 2) { // jesli nie wybrano wyjscia to wlacz dane podmenu

			menu_drugie(i);

		}

	}
	else {

		menu_glowne(i);

	}

}

void menu_drugie(int parametr) {
					   

	if (parametr == 0) { //nowa gra

		clear_screen();
		int i = 0; // domyslnie ustalona strzalka w menu na pozycji 0
		
		char nawigacja;

		do {

			clear_screen();

			cout << "Wybierz rozmiar planszy" << endl

				<< " 9x9, min:10 ";

			if (i == 0) {
		
		cout << red << " <-- " << reset;
		
		
	}

			cout << "16x16, min:40 ";

			if (i == 1) {
		
				cout << red << " <-- " << reset;
		
			}

			cout << "16x30, liczba min: 99 ";

			if (i == 2) {
		
				cout << red << " <-- " << reset;
		
			}
			else {

				cout << endl; // znak zachety ponizej

			}


			do {

				nawigacja = _getch(); // pobiera znak tak dlugo az zostana wcisniete strzalki gora/dol lub enter lub ESC(27)

			} while (nawigacja != 80 && nawigacja != 72 && nawigacja != 13 && nawigacja != 27);



			if (nawigacja == 80) { // w dol

				if (i >= 2) {

					i = 0;

				}
				else {

					i++;

				}

			}
			else if (nawigacja == 72) { // w gore

				if (i <= 0) {

					i = 2;

				}
				else {

					i--;

				}

			}
			else if (nawigacja == 27) { // ESC - wyjscie do menu glownego

				menu_glowne();

			}
			else if (nawigacja == 13) { //enter, wlaczenie trybu gry o danym numerze w zmiennej i



				clear_screen();

				if (i == 0) { // 9x9

					ry = rx = 9;

					liczba_min = 10;

				}
				else if (i == 1) { //16x16

					ry = rx = 16;

					liczba_min = 40;

				}
				else if (i == 2) { //16x30

					ry = 16; // wierszy

					rx = 30; // kolumn

					liczba_min = 99;

				}

				tab0 = new char*[ry];

				tab1 = new char*[ry];

				for (int i = 0; i<ry; i++) {

					*(tab0 + i) = new char[rx];

					*(tab1 + i) = new char[rx];



					for (int x = 0; x<rx; x++) {

						tab0[i][x] = char(176); // wstawiamy do tablicy ukrytej znaczek pola odslonietego, niektore z tych pol nadpiszemy minami i numerkami o liczbie min wokolo

						tab1[i][x] = char(219); // wstawiamy do tablicy widocznej dla gracza znaczek zaslonietego pola						

					}

				}



				// losujemy i wstawiamy miny do ukrytej planszy

				int losowe_pole_y;

				int losowe_pole_x;

				int i = 0;

				srand(time(NULL)); // inicjujemy ziarno dla generatora liczb losowych

				do {

					losowe_pole_y = rand() % ry;

					losowe_pole_x = rand() % rx;

					if (tab0[losowe_pole_y][losowe_pole_x] != char(42)) { // jesli w wylosowanym polu nie ma jeszcze miny to wstawiamy tam mine

						tab0[losowe_pole_y][losowe_pole_x] = char(42); // wstawiamy mine do wylosowanego pola

						//cout<<losowe_pole_y<<", x: "<<losowe_pole_x<<endl;

						i++;

					}

					//cout<<"        "<<i<<" ----- "<<losowe_pole_y<<", x: "<<losowe_pole_x<<endl;

				} while (i<liczba_min);

				//wstawiamy do planszy ukrytej liczby o minach znajdujacych sie wokolo

				int zi, zx; // zmienne do operowania wokol pola, ktorego szukamy miny

				int z_miny; // liczba znalezionych min wokol pola

				for (int i = 0; i<ry; i++) {

					for (int x = 0; x<rx; x++) {

						z_miny = 0; // resetujemy liczbe min wokol pola



						if (tab0[i][x] != 42) { // pole dla ktorego liczby liczbe min wokol nie moze byc mina


							//# Sprawdzamy 3 pola nad komorka i,x

							zi = i - 1; // pole wyzej

							if (zi >= 0) {

								if (tab0[zi][x] == 42) { // jesli w tym polu jest mina to zwiekszamy licznik min

									z_miny++;

								}


								zx = x + 1; // pole wyzej i jedna komorka w prawo

								if (zx<rx) { // kolumna nie moze wystawac poza plansze

									if (tab0[zi][zx] == 42) {

										z_miny++;

									}

								}

								zx = x - 1; // pole wyzej i jedna komorka w lewo

								if (zx >= 0) { // kolumna nie moze wystawac poza plansze

									if (tab0[zi][zx] == 42) {

										z_miny++;

									}

								}

							}



							//# Sprawdzamy pola po prawej i lewej nad komorka i,x

							zx = x + 1; // jedna komorka w prawo

							if (zx<rx) {

								if (tab0[i][zx] == 42) { // jesli w tym polu jest mina to zwiekszamy licznik min

									z_miny++;

								}

							}



							zx = x - 1; // jedna komorka w lewo

							if (zx >= 0) {

								if (tab0[i][zx] == 42) { // jesli w tym polu jest mina to zwiekszamy licznik min

									z_miny++;

								}

							}





							//# Sprawdzamy 3 pola pod komorka i,x

							zi = i + 1; // pole wyzej

							if (zi<ry) {

								if (tab0[zi][x] == 42) { // jesli w tym polu jest mina to zwiekszamy licznik min

									z_miny++;

								}



								zx = x + 1; // pole nizej i jedna komorka w prawo

								if (zx<rx) { // kolumna nie moze wystawac poza plansze

									if (tab0[zi][zx] == 42) {

										z_miny++;

									}

								}

								zx = x - 1; // pole nizej i jedna komorka w lewo

								if (zx >= 0) { // kolumna nie moze wystawac poza plansze

									if (tab0[zi][zx] == 42) {

										z_miny++;

									}

								}

							}



							// jesli liczba min wokol pola jest wieksza niz 0 to wstawiamy numerek do pola i,x o liczbie min wokolo

							switch (z_miny) {

							case 1:

								tab0[i][x] = '1';

								break;

							case 2:

								tab0[i][x] = '2';

								break;

							case 3:

								tab0[i][x] = '3';

								break;

							case 4:

								tab0[i][x] = '4';

								break;

							case 5:

								tab0[i][x] = '5';

								break;

							case 6:

								tab0[i][x] = '6';

								break;

							case 7:

								tab0[i][x] = '7';

								break;

							case 8:

								tab0[i][x] = '8';

								break;

							case 9:

								tab0[i][x] = '9';

								break;

							}



						}

					}



				}
				
				liczba_odsloniec = czas_gry = 0;
				liczba_flag = liczba_min;

				run_game();
				




			}
			else {

				cout<<"(Error 1) Nieoczekiwany blad programu!";
			}

		} while (nawigacja != 13); // wykonuje obsluge menu az do momentu wcisniecia entera


	}
	else if (parametr == 1) {

				clear_screen();
		
				ifstream plik;
				plik.open("save_saper.txt",ios::in);
				
				string wiersz;
				int licznik = 0;
				while(getline(plik, wiersz))
				{
					licznik++;
					if(licznik == 1)
					plik >> rx;
					else if(licznik == 2)
					plik >> ry;
					else if(licznik == 3)
					plik >> liczba_min;
					else if(licznik == 4)
					plik >> czas_gry;
					else if(licznik == 5)
					plik >> liczba_odsloniec;
					else if(licznik > 5)
					break;
				}
				plik.close();
				
				
				tab0 = new char*[ry];

				tab1 = new char*[ry];

				for (int i = 0; i<ry; i++) {

					*(tab0 + i) = new char[rx];

					*(tab1 + i) = new char[rx];


				}
				
				ifstream plik2;
				plik2.open("save2_saper.txt",ios::in);
				
				for (int y = 0; y < ry; y++){
					for (int x = 0; x < rx; x++){
						plik2 >> tab0[y][x];
					}
				}
				
				plik2.close();
				
				ifstream plik3;
				plik3.open("save3_saper.txt",ios::in);
				
				for (int y = 0; y < ry; y++){
					for (int x = 0; x < rx; x++){
						plik3 >> tab1[y][x];
					}
				}
				
				plik3.close();
				
				liczba_flag = liczba_min;

				run_game();

	
	}



}

void run_game(int komunikat) {
	
	czas_gry2 = 0;
	
	static int liczba_ruchow = 0; // zawiera informacje ile razy wcisnieto strzalke

	static int zi, zx; // zmienne sluzace do okreslania podswietlonego elementu

	char nawigacja;


	clear_screen();

	

	if (liczba_ruchow == 0) {

		zi = zx = 0; // domyslnie ustalona pozycja podswietlonego elementu

	}


	if (liczba_odsloniec >= 1) { // obliczamy czas gry dopiero po pierwszym ruchu

		czas_gry2 = time(NULL)-czas_gry3;

	}
	
	
	if (char(83) || char(115)){
		
		czas_gry = czas_gry + czas_gry2;
		
		fstream plik;
		plik.open("save_saper.txt", ios::out);
		
		plik << endl;
		plik << rx << endl;
		plik << ry << endl;
		plik << liczba_min << endl;
		plik << czas_gry << endl;
		plik << liczba_odsloniec << endl;
		
		plik.close();
		
		czas_gry=0;
		
		fstream plik2;
		plik2.open("save2_saper.txt", ios::out);

		for (int y = 0; y < ry; y++){
			for (int x = 0; x < rx; x++){
				plik2 << tab0[y][x];
			}
		}

		plik2.close();
		
		fstream plik3;
		plik3.open("save3_saper.txt", ios::out);

		for (int y = 0; y < ry; y++){
			for (int x = 0; x < rx; x++){
				plik3 << tab1[y][x];
			}
		}

		plik3.close();
	}

	if (komunikat == 1) { // przegrana -koniec gry

		for (int i = 0; i<ry; i++) {

			for (int x = 0; x<rx; x++) {

				if (tab0[i][x] == char(42)) {


					cout << tab0[i][x];


				}
				else {

					cout << tab0[i][x];

				}

			}

			cout << endl;

		}


		cout << "PRZEGRANA! ";





	}
	else if (komunikat == 2) { // wygrana - koniec gry

		for (int i = 0; i<ry; i++) {

			for (int x = 0; x<rx; x++) {

				if (tab0[i][x] == char(42)) {


					cout << tab0[i][x];


				}
				else {

					cout << tab0[i][x];

				}

			}

			cout << endl;

		}


		cout << "WYGRANA! Gratulacje! ";





	}



	if (komunikat == 1 || komunikat == 2) {
		
		czas_gry = czas_gry + czas_gry2;
		cout << "Czas gry:" << czas_gry << "s Liczba min: " << liczba_flag;











		//nalezy zresetowac liczbe ruchow i odsloniec na koniec gry

		liczba_ruchow = liczba_odsloniec = 0;
		
		//niszczymy tablice dynamiczna

		for (int i = 0; i<ry; ++i) {

			delete[] tab0[i];

			delete[] tab1[i];

		}

		delete[] tab0;

		delete[] tab1;






		cout << endl << "Nacisnij enter aby przejsc do menu.";

		do {

			nawigacja = _getch(); // pobiera znak enter/spacja lub ESC(27) aby wyjsc do menu

		} while (nawigacja != 13 && nawigacja != 32 && nawigacja != 27);



		menu_glowne();

	}



	if (komunikat == 0) {



		for (int i = 0; i<ry; i++) {

			for (int x = 0; x<rx; x++) {

				if (zi == i && zx == x) { // kolorujemy na czerwono element na ktorym jest zaznaczony

					cout << red << tab1[i][x] << reset;
					

				}
				else if (tab1[i][x] == 'F' || tab1[i][x] == '?') {


					cout << red << tab1[i][x] << reset;
					

				}
				else {

					cout << tab1[i][x];

				}

			}

			cout << endl;
		}



		cout << "Liczba min: " << liczba_flag;

		do {

			nawigacja = _getch(); // pobiera znak tak dlugo az zostana wcisniete strzalki gora/dol/lewo/prawo lub enter/spacja lub ESC(27), 102-F 118-V

		} while (nawigacja != 80 && nawigacja != 72 && nawigacja != 75 && nawigacja != 77 && nawigacja != 13 && nawigacja != 32 && nawigacja != 27 && nawigacja != 102 && nawigacja != 118);



		if (nawigacja == 80) { // w dol		

			if (zi == (ry - 1)) { // jesli obecnie podswietlone pole jest ustawione na ostatnim wierszu to klikniecie w dol oznacza przeskoczenie do pierwszego wiersza

				zi = 0;

			}
			else {

				zi++;

			}

			liczba_ruchow++;

			run_game();

		}
		else if (nawigacja == 72) { // w gore

			if (zi == 0) { // jesli jestesmy w pierwszym wierszu to strzalka w gore przesuwa nas na ostatni wiersz

				zi = ry - 1; // -1 bo tablica jest od indexu 0

			}
			else {

				zi--;

			}

			liczba_ruchow++;

			run_game();

		}
		else if (nawigacja == 75) { // w lewo

			if (zx == 0) { // jesli jestem w pierwszej kolumnie to po wcisnieciu strzalki w lewo przenosi mnie do ostatniej kolumny

				zx = rx - 1;

			}
			else {

				zx--;

			}

			liczba_ruchow++;

			run_game();

		}
		else if (nawigacja == 77) { // w prawo

			if (zx == (rx - 1)) { // jesli jestem w ostatniej kolumie to strzalka w prawo przenosi mnie do pierwszej

				zx = 0;

			}
			else {

				zx++;

			}

			liczba_ruchow++;

			run_game();

		}
		else if (nawigacja == 27) { // ESC - wyjscie do menu glownego

			liczba_ruchow  = liczba_odsloniec = 0;
			
			menu_glowne();

		}
		else if (nawigacja == 32 || nawigacja == 13) { //spacja lub enter sluzy do odslaniania pola

			liczba_ruchow++;



			if (tab1[zi][zx] != tab0[zi][zx]) { // jesli po raz pierwszy odslaniamy pole


				if (tab0[zi][zx] != char(42)) { // odsloniamy pole ktore nie jeste mina

					liczba_odsloniec++; // operacja odsloniecia

            	if(liczba_odsloniec==1) { // jesli po raz pierwszy odslonieto pole to od tego momentu liczymy czas

                	czas_gry3 = time(NULL);

            	}

					odslon_pola_wokol(zi, zx);



					// wykonujemy sprawdzenie czy wygrano juz gre

					int czy_wygrano = 1; // 1 - tak, jesli zmienna zawiera 0 to znaczy ze ktores pole nie zawierajace miny jest nie odkryte				

					for (int i = 0; i<ry; i++) {

						if (czy_wygrano) {

							for (int x = 0; x<rx; x++) {

								if (tab0[i][x] != char(42)) { // jesli pole nie jest mina to sprawdzamy czy zostalo odkryte

									if (tab1[i][x] != tab0[i][x]) { // jesli odkryte pole jest rozne od ukrytego to znaczy ze jeszcze cala plansza nie zostala odkryta

										czy_wygrano = 0;

										break; // przerywamy sprawdzenie poniewaz jesli jakies pole jest nie odkryte to automatycznie nie ma sensu dalsze sprawdzanie

									}

								}

							}

						}
						else {

							break; // przerywamy sprawdzenie jesli zmieniono wartosc czy_wygrano na 0

						}

					}



					if (czy_wygrano) {

						run_game(2); // parametr 2 - wygrana koniec gry 	

					}
					else {

						run_game();

					}



				}
				else if (tab0[zi][zx] == char(42)) { //mina - koniec gry

					tab1[zi][zx] = tab0[zi][zx];

					run_game(1); // parametr 1 - przegrana koniec gry

				}

			}
			else { // odslaniamy pole kotre jest juz odsloniete wiec nic nie robimy tylko odswiezamy plansze

				run_game();

			}



		}
		else if (nawigacja == 102) { // F - wstawiamy flage

			if (tab1[zi][zx] == char(219) || tab1[zi][zx] == '?') { // jesli pole jest zasloniete lub jest na nim pytajnik to wstawiamy na nie F

				tab1[zi][zx] = 'F';

				liczba_flag--;

			}
			else if (tab1[zi][zx] == 'F') { // jesli na polu jest juz flaga to ja zdejmujemy

				tab1[zi][zx] = 219; // ustawiamy zasloniete pole

				liczba_flag++;

			}

			liczba_ruchow++;

			run_game();

		}
		else if (nawigacja == 118) { // V - wstawiamy pytajnik

			if (tab1[zi][zx] == char(219)) { // jesli pole jest zasloniete to wstawiamy na niego pytajnik

				tab1[zi][zx] = '?';

			}
			else if (tab1[zi][zx] == 'F') { // jesli jest na polu flaga to wstawiamy na niego pytajnik i zwiekszamy liczbe dostepnych flag

				tab1[zi][zx] = '?';

				liczba_flag++;

			}
			else if (tab1[zi][zx] == '?') { // jesli na polu jest juz pytajnik to go zdejmujemy

				tab1[zi][zx] = 219; // ustawiamy zasloniete pole

			}

			liczba_ruchow++;

			run_game();

		}



	}

}

void odslon_pola_wokol(int zi, int zx) {



	//zi>=0 && zi<ry && zx>=0 && zx<rx

	if (tab1[zi][zx] == char(219) || tab1[zi][zx] == 'F' || tab1[zi][zx] == '?') { //w tablicy widocznej jest polem zaslonietym/F/? to odslon go

		tab1[zi][zx] = tab0[zi][zx];



		if (tab0[zi][zx] == char(176)) { //jesli pole jest puste w tablicy ukrytej to odslon pola wokol niego		

			int zi_p1 = zi + 1;

			int zi_m1 = zi - 1;

			int zx_p1 = zx + 1;

			int zx_m1 = zx - 1;


			if (zi_m1 >= 0 && zx_m1 >= 0) {

				odslon_pola_wokol(zi_m1, zx_m1); //gora lewo

			}

			if (zi_m1 >= 0) {

				odslon_pola_wokol(zi_m1, zx); // gora

			}

			if (zi_m1 >= 0 && zx_p1<rx) {

				odslon_pola_wokol(zi_m1, zx_p1); // gora prawo

			}

			if (zi_p1<ry && zx_m1 >= 0) {

				odslon_pola_wokol(zi_p1, zx_m1); // dol lewo

			}

			if (zi_p1<ry) {

				odslon_pola_wokol(zi_p1, zx); // dol 

			}

			if (zi_p1<ry && zx_p1<rx) {

				odslon_pola_wokol(zi_p1, zx_p1); // dol prawo

			}

			if (zx_m1 >= 0) {

				odslon_pola_wokol(zi, zx_m1); // lewo		

			}

			if (zx_p1<rx) {

				odslon_pola_wokol(zi, zx_p1); // prawo

			}

		}

	}

}

