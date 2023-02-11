#include<iostream>
using namespace std;

bool czy_pierwsza(int n)
{
  if(n<2)
    return false;

  for(int i=2;i*i<=n;i++)
    if(n%i==0)
      return false;

  return true;
}

int main()
{
  int d;
  cin >> d;
  int n;
 for(int i=0; i<d;i++){
  cin>>n;

  if(czy_pierwsza(n))
    cout<<"PIERWSZA"<<endl;
  else
    cout<<"ZLOZONA"<<endl;
 }
  return 0;
}
