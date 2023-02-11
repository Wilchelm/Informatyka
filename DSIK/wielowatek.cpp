#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>

/* Definicja funkcji, której kod okreœlony jest poni¿ej */

void *wypisz_wiadomosc( void *ptr );

int main()
{
	pthread_t threads[2];
	const char *wiadomosc1 = "W¹tek 1";
	const char *wiadomosc2 = "W¹tek 2";
	int  tid[2];

	/* Utworzenie dwóch niezale¿nych w¹tków, ka¿dy uruchomi funkcjê wypisz_wiadomosc */

	tid[0] = pthread_create( &threads[0], NULL, wypisz_wiadomosc, (void*) wiadomosc1);
	tid[1] = pthread_create( &threads[1], NULL, wypisz_wiadomosc, (void*) wiadomosc2);

	/* Funkcja main musi poczekaæ na zakoñczenie obu w¹tków, po to by nie powsta³y procesy Zombie */

	pthread_join( threads[0], NULL);
	pthread_join( threads[1], NULL);

	printf("W¹tek 1 zwraca: %d\n",tid[0]);
	printf("W¹tek 2 zwraca: %d\n",tid[1]);
	exit(0);
}

void *wypisz_wiadomosc( void *ptr )
{
char *message;
message = (char *) ptr;
printf("%s \n", message);
}
