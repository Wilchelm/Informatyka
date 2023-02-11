#include <stdio.h>
#include <string.h>

int main()
{
	char * zmienna;
	scanf("%s", &zmienna);
	int wynik;
	wynik = toInt(zmienna);
	printf("%d",wynik);
	return 0;
}

int toInt(char * xyz)
{
	int liczba=0;
	int i=0;
	for(i;i<strlen(xyz);i++)
		if(xyz[i]>='0' && xyz[i]<= '9')
			liczba = 10*liczba + (xyz[i]-'0');
	return liczba;
}
