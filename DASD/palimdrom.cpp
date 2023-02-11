#include <iostream>
#include <cmath>
int main()
{
int liczba, cyfry, kroki;
std::cin>>liczba;
cyfry=0;  
kroki=liczba;  
if(kroki==0)  
cyfry=1;  
else    
while(kroki>0)  
{  
cyfry++;  
kroki/=10;
}  
int odwrocona=0;
for(int i=0;i<cyfry;i++)
{
odwrocona+=pow(10.0, cyfry-1-i)*(liczba%10);
liczba=liczba/10;
}
std::cout<<odwrocona;
return 0;
}
