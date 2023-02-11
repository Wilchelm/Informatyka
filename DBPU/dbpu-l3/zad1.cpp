#include <iostream>

using namespace std;

int main(){
	int abc[30];  //*** stack smashing detected ***: <unknown> terminated w celu popracy zamiana z abc[10] na abc[30]
	int def[10];

	for(int i=0;i<30;i++) abc[i]=i;
        
	for(int i=0;i<10;i++) {
            def[i]=i; //ERROR SUMMARY: 112 errors from 4 contexts (suppressed: 0 from 0) podstawienie wartości  w celu likwidacji odczytu niezainicjalizowanych zmiennych
            cout << def[i] << endl;
        }
}
