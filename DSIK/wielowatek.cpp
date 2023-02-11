#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

/* Definicja funkcji, kt�rej kod okre�lony jest poni�ej */

void *wypisz_wiadomosc( void *ptr );

int main()
{
	pthread_t threads[2];
	const char *wiadomosc1 = "W�tek 1";
	const char *wiadomosc2 = "W�tek 2";
	int  tid[2];

	/* Utworzenie dw�ch niezale�nych w�tk�w, ka�dy uruchomi funkcj� wypisz_wiadomosc */

	tid[0] = pthread_create( &threads[0], NULL, wypisz_wiadomosc, (void*) wiadomosc1);
	tid[1] = pthread_create( &threads[1], NULL, wypisz_wiadomosc, (void*) wiadomosc2);

	/* Funkcja main musi poczeka� na zako�czenie obu w�tk�w, po to by nie powsta�y procesy Zombie */

	pthread_join( threads[0], NULL);
	pthread_join( threads[1], NULL);

	printf("W�tek 1 zwraca: %d\n",tid[0]);
	printf("W�tek 2 zwraca: %d\n",tid[1]);
	exit(0);
}

void *wypisz_wiadomosc( void *ptr )
{
char *message;
message = (char *) ptr;
printf("%s \n", message);
}
