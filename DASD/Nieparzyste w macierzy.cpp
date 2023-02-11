#include<iostream>	
using namespace std;

int main()
{
	int d;
	cin >> d;
	for(int D=0;D<d;D++)
	{
		int kolumny,rzedy;
		cin >> rzedy >> kolumny;
		int tab[rzedy][kolumny];
		for(int i=0; i<rzedy;i++)
		{
			for(int j=0; j<kolumny;j++)
			{
				cin >> tab[i][j];
				if(tab[i][j]%2!=0)
				cout << tab[i][j] <<" ("<< j+1 <<","<< i+1 <<")"<< endl;
			
			}
		}
	}
	return 0;
}
