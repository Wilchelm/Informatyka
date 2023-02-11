#include<iostream>
int main()
{
int a, n, wynik=1;
std::cin>>a>>n;
for(int i=0;i<n;i++)
{
	wynik*=a;
}
std::cout<<wynik;
return 0;
}
