#include <iostream>
#include <stdlib.h>
#include <time.h>
using namespace std;

const int maxx = 8;//definiujemy maksimum jako stałą
int lab[8][8];

//funkcja do liczenia liczby ścian
int pom(int a, int b, int z) {
	int pom=0;
	if ((a < maxx)&&(lab[a+1][b]==z)){
		pom++;
		}
	if ((b < maxx)&&(lab[a][b+1]==z)){
		pom++;
		}
	if ((a > 0)&&(lab[a-1][b]==z)){
		pom++;
		}
	if ((b > 0)&&(lab[a][b-1]==z)){
		pom++;
		}
	return pom;
	}

int main(){



	for(int i=0;i<8;i++){//wczytywanie labiryntu z pliku
		for(int j=0;j<8;j++){
			cin >> lab[i][j];
			cout << lab[i][j] << " ";
			}
		cout << endl;
		}
	cout << endl;

	int x=0,y=0;//pozycja gracza
	lab[x][y]=4;//tu dodałem, że po wejściu już zaznaczmy pole

	for(int k=0;k<40;k++){//przechodzenie przez labirynt
		if ((x == 3) && (y == 7)){ // Tu zmieniłem parametr wyjścia z labiryntu bo były niepoprawne
			cout << " wyszedłeś z labiryntu " << endl; // Tu brakowało linii
			for(int i=0;i<8;i++){//wczytywanie labiryntu z pliku --> cat labirynt(nazwa pliku)| ./a.out
				for(int j=0;j<8;j++){
					cout << lab[i][j] << " ";
					if (lab[i][j]==8) {
						lab[i][j]=0;
						}
					}
				cout << endl;
				}
			exit (0);
			}

		//Tu sprawdzam czy jest ślepy zaułek i pamietam go
		if (pom(x,y,1) > 2) {
			lab[x][y]=3;
			}

		// ograniczam liczbę kroków "do przodu"
		int krok=0;
		if ((x > 0)&&(lab[x-1][y]==0)&&(krok==0)){
			krok++;
			x--;
			lab[x][y] = 4;
			}
		if ((y < maxx)&&(lab[x][y+1]==0)&&(krok==0)){
			krok++;
			y++;
			lab[x][y] = 4;
			}
		if ((x < maxx)&&(lab[x+1][y]==0)&&(krok==0)){
			krok++;
			x++;
			lab[x][y] = 4;
			}
		if ((y > 0)&&(lab[x][y-1]==0)&&(krok==0)){
			krok++;
			y--;
			lab[x][y] = 4;
			}


		//tu dodałem cofanie z "zapamiętywaniem"
		if ((x < maxx)&&(lab[x+1][y]==4)&&(lab[x][y]==3)){
			x++;
			if (pom(x,y,1) == 2) {
				lab[x][y]=3;
				}
			if (pom(x,y,3) >= 2) {
				lab[x][y]=3;
				}
			}
		if ((y < maxx)&&(lab[x][y+1]==4)&&(lab[x][y]==3)){
			y++;
			if (pom(x,y,1) == 2) {
				lab[x][y]=3;
				}
			if (pom(x,y,3) >= 2) {
				lab[x][y]=3;
				}
			}
		if ((x > 0)&&(lab[x-1][y]==4)&&(lab[x][y]==3)){
			x--;
			if (pom(x,y,1) == 2) {
				lab[x][y]=3;
				}
			if (pom(x,y,3) >= 2) {
				lab[x][y]=3;
				}
			}
		if ((y > 0)&&(lab[x][y-1]==4)&&(lab[x][y]==3)){
			y--;
			if (pom(x,y,1) == 2) {
				lab[x][y]=3;
				}
			if (pom(x,y,3) >= 2) {
				lab[x][y]=3;
				}
			}


		for(int i=0;i<8;i++){//wczytywanie labiryntu z pliku
			for(int j=0;j<8;j++){
				cout << lab[i][j] << " ";
				if (lab[i][j]==8) {
					lab[i][j]=0;
					}
				}
				cout << endl;
			}
	/*
To jest bez sensu bo jak wcześniej sprawdza czy wyszedł to wtedy kończy program (exit (0);)
		for(int k=0;k<40;k++){//przechodzenie przez labirynt
			if ((x == 3) && (y == 7)){
				cout << " wyszedłeś z labiryntu " << endl;
				}
			}
*/
		cout << "x=" << x << "y=" << y  << endl;
		}
	cout << "Brak wyjścia" << endl;
	}
