#include<iostream>

int funkcja(int a, int b)
{
if(a==b || b==0) return 1;
else return funkcja(a-1,b-1)+funkcja(a-1,b);
}

int main()
{
int d,n,k;
std::cin>>d;
for(int i=0;i<d;i++)
{
std::cin>>n>>k;
std::cout<<funkcja(n,k);
}
return 0;
}


