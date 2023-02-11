#include <iostream>
#include "komputer.h"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */
using namespace std;

int main(int argc, char** argv) {
	
	Komputer * k = new Komputer  ("dell", 3, 2);
	
	cout << k->wypisz();
	
	Komputer * nowy = new Komputer(*k);
	
	cout << nowy->wypisz();
	
	delete k;
	return 0;
}
