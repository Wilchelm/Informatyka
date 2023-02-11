#include <iostream>
using namespace std;

int main ()
{
	int x,y,k,kwiaty,liscie;
	for (int i=0; i<20; ++i)
	{
		cin >> x;
		y = x;
		k=0;
		kwiaty = 0;
		liscie = 0;
		if (x==0)
		{
			break;
		}
		else
		{
			while (y!=1)
			{
				if (y % 2 == 0)	
				{
					y = y/2;
					++k;
					++kwiaty;
				}
				else
				{
					y = 3*y + 1;
					++k;
					++liscie;
				}
			}
			if (k<=15)
			{
				cout << "TAK " << kwiaty << " " << liscie << endl;
			}	
			else
			{
				cout << "NIE" << endl;
			}
		}
	}
	return 0;
}
