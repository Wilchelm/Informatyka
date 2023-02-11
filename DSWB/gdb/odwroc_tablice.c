#include <stdio.h>
#include<math.h>

void wyswietl(int *t, int length) {
   printf("\n");
   int i=0;
   for (int i=0; i<length; i++) {
      printf("%d ", t[i]);
   }
}

int main ()
{
    int n=0;
    printf("Tablice... znajdz wszystkie bledy :)\n");
    printf("Podaj Dlugosc tablicy od 0 do 100 \n");
    scanf("%d", &n);
    
    int *tablica = new int[n];
	int *tablica2 = new int[n];
    int i =0;
    for(int i=0; i<n; i++) {
      tablica[i]=i;
    }
    
    
    
    printf("Aktualna tablica to:  \n");
    wyswietl(tablica, 5);
    
    printf("\n odracamy tabice");
    
    for (int i=0; i<n; i++) {
       int temp = tablica[i];
       tablica[i] = tablica[n-i-1];
       tablica[n-i-1] = temp;
    } // algorytm podwujnie odwraca tablice w efekcie zwraca taka sama tablice

 	for (int i=0; i<n; i++) {
       tablica2[i] = tablica[n-i-1];
    }
    
    printf("Odwrocana tablica to: wszystko ok?: ");
    wyswietl(tablica2, n);
    return 0;
}
