#include<iostream>
#include<string>
using namespace std;

int main() 
{
	string slowo;
	int n;
	cin >> n;
	for(int i = 0; i<n ; i++)
	{
		int j = 0;
		cin >> slowo;
				
		for(int i = slowo.size()-1 ; i >= 0; i--)
		{
			if(slowo[j]==slowo[i])
			{
				j++;
			}
		}
		if(j == slowo.size())
		{
			cout << slowo << "==" << slowo;
		}
		if(j != slowo.size())
		{
			cout << slowo << "!=";
			for(int i = slowo.size()-1 ; i >= 0; i--)
			{
				cout << slowo[i];
			}
		}
	}
	
return  0;	

}
