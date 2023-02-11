#include<iostream>
using namespace std;
 
int main()
{
	int n;
	cin >> n;
	int tablica[n];
	for(int i=0;i<n;i++)
	{
		cin >> tablica[i];
	}
	int liczba, l, p, s;
	int d;
	cin >> d;
	for(int j=0;j<d;j++)
	{
		cin >> liczba;
		l = 0;
		p = n-1;
		while (true)
			{
			if (l > p)
			{
			cout << "NIEOBECNY" << endl;
			break;
			}
			s = (l+p)/2;
			if (tablica[s] == liczba)
			{
			cout << s+1 << endl;
			break;
			}
			else if (tablica[s] < liczba)
			l = s+1;
			else
			p = s-1;
			}
	}
	return 0;
}
