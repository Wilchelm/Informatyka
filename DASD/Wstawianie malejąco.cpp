#include<iostream>
using namespace std;

int main()
{
	int n, tymczasowa, i, j;
	cin >> n;
	int *tablica = new int[n];

	for (i = 0; i < n; i++)
	{
		cin >> tablica[i];
	}

	for (i = 1; i < n; i++)
	{
		tymczasowa = tablica[i];
		for (j = i - 1; j >= 0; j--)
		{
			if (tymczasowa < tablica[j])
				break;
			else
				tablica[j + 1] = tablica[j];
		}
		tablica[j + 1] = tymczasowa;
	}

	for (i = 0; i < n; i++)
		cout << tablica[i] <<" ";

	delete[] tablica;

	return 0;
}
