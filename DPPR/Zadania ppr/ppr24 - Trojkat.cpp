#include<iostream>
#include <cmath>
using namespace std;

double kat(double a, double b, double c)
{
        double cos_kat;
        cos_kat = (b * b + c * c - a * a) / (2 * b * c);
        return(acos(cos_kat) * 180 / 3.14159265);
}
int main()
{
	int x;
	cin >> x;
	for(int i=0;i<x;i++)
	{ 
		double a, b, c, c2;
		cin >> a >> b;
		c2 = a*a + b*b;
		c=sqrt(c2);
		if (kat(b,c,a) == kat(a,b,c))
            {
                cout << ceil(c) << " " << round(kat(b,c,a)) << endl;
            }
        else if (kat(b,c,a) > kat(a,c,b))
            {
                cout << ceil(c) << " " << round(kat(a,c,b)) << endl;
            }
        else
            {
                cout << ceil(c) << " " << round(kat(b,c,a)) << endl;
            }
	}
	return 0;
}
