#include <iostream>  
using namespace std; 

int main() 
{ 
int n,suma_dzielnikow=0;  
 cin>>n; 
 for (int i=1;i<n;++i) 
 if (n%i==0) 
 suma_dzielnikow=suma_dzielnikow+i; 
 if (suma_dzielnikow==n) 
 cout<<"tak"<<endl; 
 else 
 cout<<"nie"<<endl; 
 
 return 0; 
}
