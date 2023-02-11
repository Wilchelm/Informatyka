#include <iostream>
#include <string>

using namespace std;

int main()
{
    int n;
   	string wyraz;
    cin >> n;
    
    cin.ignore();
    string * tablica_wyrazow = new string[ n ];
   	int wynik = 0;
    
    for( int i = 0; i < n; i++ )
    {
        
        getline( cin, tablica_wyrazow[ i ] );
    }
   
   	getline( cin, wyraz );
    
    for( unsigned a = 0; a < n; a++ )
    {
        if( tablica_wyrazow[ a ] == wyraz ) ++wynik;
   }
    
   cout << wynik << endl;
   delete[] tablica_wyrazow;
    
    return 0;
}
