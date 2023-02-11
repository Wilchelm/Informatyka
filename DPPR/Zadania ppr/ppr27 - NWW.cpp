#include<iostream>
 using namespace std;
 
int NWD(int a, int b)
{
    int c;
    while (b != 0)
    {
          c = a % b;
          a = b;
          b = c;
    }
    return a;
}

int main()
{
	int x;
	cin >> x;
	for(int j=0; j<x; j++)
	{
		int temp1, temp2, wynik;
		int tab[4];
		for(int i=0; i<4;i++)
		{
			cin >> tab[i];
		}	
		temp1 = (tab[0]*tab[1])/NWD(tab[0],tab[1]);
		temp2 = (tab[2]*tab[3])/NWD(tab[2],tab[3]);
		wynik = (temp1*temp2)/NWD(temp1, temp2);
		cout << wynik << endl;
	}	
	return 0;
}
