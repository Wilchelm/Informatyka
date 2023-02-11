#include <iostream>

using namespace std;

int main(){
double suma = 0;
int bramka = 0;
double tab[3];
double tab2[2];

cout << "Podaj nazwe bramki: '1' : AND, '2': NOT, '3': NAND, '4' : OR\n";
cin >> bramka;

//AND
switch(bramka)
    {
    case 1:         //AND
        {
            double u[3] = {0,0,1};
            double x,y;
            x = 1.0/3.0;
            y = -1.0/2.0;
            tab[0] = x;
            tab[1] = x;
            tab[2] = y;
            for(int i = 0; i < 3; i++)
            {
                suma = suma + tab[i]*u[i];
            }
            if(suma >= 0)
            {
                cout << "1" << "\n";
            }
            else
            {
                cout << "0" << "\n";
            }
            suma = 0;
        }
    break;

    case 2:         //NOT
        {
            tab2[0] = 1;
            tab2[1] = -2;
            double ul[2] = {1,1};

            for(int i = 0; i < 2; i++)
            {
                suma = suma + tab2[i]*ul[i];
            }
            if(suma >= 0)
            {
                cout << "1" << "\n";
            }
            else
            {
                cout << "0" << "\n";
            }
            suma = 0;
            break;
        }

    case 3:         //NAND
        {
            double u[3] = {1,1,1};
            double x,y;
            tab[0] = -3;
            tab[1] = -3;
            tab[2] = 5;
            for(int i = 0; i < 3; i++)
            {
                suma = suma + tab[i]*u[i];
            }
            if(suma >= 0)
            {
                cout << "1" << "\n";
            }
            else
            {
                cout << "0" << "\n";
            }
            suma = 0;
        }
    break;

    case 4:         //OR
        {
            double u[3] = {0,0,1};
            double x,y;
            tab[0] = 2;
            tab[1] = 2;
            tab[2] = -1;
            for(int i = 0; i < 3; i++)
            {
                suma = suma + tab[i]*u[i];
            }
            if(suma >= 0)
            {
                cout << "1" << "\n";
            }
            else
            {
                cout << "0" << "\n";
            }
            suma = 0;
        }
    break;
    }
//cout << u[0]*w[0];
}
