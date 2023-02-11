#include <iostream>
#include <cmath>
#include <iomanip>
 
using namespace std;
 
double srodki(int xb, int xa, int yb, int ya)
{
       double c=0;
       c=sqrt(((xb-xa)*(xb-xa))+((yb-ya)*(yb-ya)));
       return c;
};
 
struct odleglosc
{
       int y;
       int x;
       int r;     
};
struct pary
{
       int a;
       int b;
};
 
int main()
{
	int l_kol;
	cin >> l_kol;
	odleglosc * ab=new odleglosc[l_kol];
    for (int i=0; i<l_kol; ++i)
    {
        cin>>ab[i].y>>ab[i].x>>ab[i].r;
    }
    int l_par=0;
    cin >> l_par;
    pary * pdo=new pary[l_par];
    for (int i=0; i<l_par; ++i)
    {
        cin>>pdo[i].a>>pdo[i].b;
    }
    for (int j=0; j<l_par; ++j)
    {     
	cout << fixed << setprecision(2) 
	<< srodki(ab[(pdo[j].b)-1].x,ab[(pdo[j].a)-1].x,ab[(pdo[j].b)-1].y,ab[(pdo[j].a)-1].y) 
	<< " ";
        if (ab[(pdo[j].a)-1].r>ab[(pdo[j].b)-1].r)
        {
           cout << fixed << setprecision(2) << 3.14*(ab[(pdo[j].a)-1].r)*(ab[(pdo[j].a)-1].r) << endl;
        }else
           cout << fixed << setprecision(2) << 3.14*(ab[(pdo[j].b)-1].r)*(ab[(pdo[j].b)-1].r) << endl;  
    }
    delete[] ab;
    delete[] pdo;
    
return 0;
}
   
