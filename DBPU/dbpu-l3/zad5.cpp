#include <iostream>

using namespace std;

int main()
{
    int telefon = 12345;    //zmienna liczbowa
    int *wsk = &telefon;    //wskaźnik wsk zawiera adres zmiennej telefon
    cout << *wsk << endl;   //wyświetlenie wyłuskanej wartości wskaźnika (12345)
    cout << wsk << endl;    //wyświetlenie adresu zmiennej telefon
    cout << &wsk << endl;   //wyświetlenie adresu wskaźnika

    wsk = NULL;             //Zerowanie pamięci?
    wsk = new int;
    wsk = &telefon;    
    cout << *wsk << endl;   //wyświetlenie wyłuskanej wartości wskaźnika (12345)
    cout << wsk << endl;    //wyświetlenie adresu zmiennej telefon
    cout << &wsk << endl;   //wyświetlenie adresu wskaźnika

/* OUTPUT:
   12345
   0x7ffd73e61a2c
   0x7ffd73e61a30
   12345
   0x7ffd73e61a2c
   0x7ffd73e61a30

Adresy są identyczne natomiast Valgrind wskazuje 
LEAK SUMMARY:
definitely lost: 4 bytes in 1 blocks
*/

    return 0;
}
