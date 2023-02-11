#include<iostream>

int powiel(int a)
{
int tab[a];
tab[0]=1;
tab[1]=1;
for(int i=2;i<a;i++)
	tab[i]=tab[i-1]+tab[i-2];
return tab[a-1];
}

int main()
{
int l;
std::cin>>l;
for(int i=0;i<l;i++)
{
int a;
std::cin>>a;
std::cout<<powiel(a);
}
return 0;
}
