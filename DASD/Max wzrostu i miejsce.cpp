#include <iostream>
using namespace std;
 
int i,a,liczba,maks,x;
 
int main ()
{
	cin>>a;
 	int tab[a];
 	for (i=1;i<=a;i++)
	 {
    cin>>liczba;
    tab[i]=liczba;
	}
 	cout<<endl;

//najwieksza
for (i=1;i<=a;i++)
{
    if (tab[i]>maks)
	{
       maks=tab[i];
	   x=i;
	}
}
cout<<maks<<" "<<x<<endl;
return 0;
}
