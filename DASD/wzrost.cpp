#include<iostream>

int main()
{
int a;
std::cin>>a;
int tab[a];
for(int i=0;i<a;i++)
{
std::cin>>tab[i];
}
int max=0;
for(int i=0;i<a;i++)
{
if(tab[i]>max) 
{
max=tab[i];
}
}
std::cout<<max;
return 0;
}
