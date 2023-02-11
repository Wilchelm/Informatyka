#include <stdio.h>
#include <stdlib.h>

typedef struct abc{
int x,y;
} liczba;

void qsort2(liczba table[], int start, int finish)
{
  int left=start,
      right=finish; 
  liczba pivot=table[(start+finish)/2];
  while(left<right) {
    // find left candidate
    while (table[left].y < pivot.y) left++;
    // find right candidate
    while (table[right].y > pivot.y) right--;
    if(left <=right) {
      liczba temp = table[left];
      table[left]=table[right];
      table[right]=temp;
       left++;
       right--;
    }
  } //while left<right
  if (start<right) qsort2(table, start, right);
  if (left<finish) qsort2(table, left, finish);
}

int main(int arc, char *argv[])
{
	char c;
	liczba a[256];
	for(int i=0; i<256;i++)
	{
	a[i].x=i;
	}
	while (c = getchar())
	{
		if (c>=0 && c<=255)
		{
		a[c].y++;
		}
	}

qsort2(a, 0,255);


for(i=0; i<255; i++)
    {
       if(a[i].y>0)
       {
            printf(a[i].x, "  ", a[i].y);
      }
    }


}




