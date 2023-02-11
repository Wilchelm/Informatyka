#include <stdio.h>

int main()
{
	for(int a=1;a<=10;a=a+1)
		{
			for (int b=1; b<=10; b=b+1)
			{
				printf("%4d \t",(a*b));
			}
		printf("\n");
		}
	getchar();
	return 0;	
}
