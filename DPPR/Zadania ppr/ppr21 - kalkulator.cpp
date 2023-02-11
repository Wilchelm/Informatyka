#include<iostream>
#include<string>
using namespace std;

int main()
{
	int n, a, b;
	string dzialanie;
	int wynik = 0;
	cin >> n;
	cin.ignore();
	for(int i=0; i<n; i++)
	{
		cin >> a;
		cin >> dzialanie;
		if(dzialanie == "+")
		{
			cin >> b;
			wynik = a+b;
			cout << wynik << endl;
		}
		if(dzialanie == "-")
		{
			cin >> b;
			wynik = a-b;
			cout << wynik << endl;
		}
		if(dzialanie == "*")
		{
			cin >> b;
			wynik = a*b;
			cout << wynik << endl;
		}
		
		
	}
	
return 0;
}
