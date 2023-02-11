#include<iostream>

using namespace std;

int main()
{
	int n = 0, m = 0, liczba = 0, sumadzielnikow = 0;
	int dzielnik[200000];
	cin >> n;
	for(int i = 0; i<n ; i++)
	{
		cin >> dzielnik[i];	
	}
	cin >> m;
for(int i = 0; i<m ;i++)\
	{
	cin >> liczba;
	for(int j = 0; j<n; j++)
		{	
		if(liczba % dzielnik[j] == 0 )
			{sumadzielnikow++;
			}
		}
cout << sumadzielnikow << endl;
sumadzielnikow = 0;
}
	return 0;
}
