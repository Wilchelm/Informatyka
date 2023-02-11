#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <stdio.h>
#include <string.h>

/* Definicja funkcji, której kod określony jest poniżej */

void *wypisz_wiadomosc( void *ptr );

int main()
{
	pthread_t threads[2];
	const char *wiadomosc1 = "Wątek 1";
	const char *wiadomosc2 = "Wątek 2";
	int  tid[2];
	int socket_client;
	
	
	
	/* Utworzenie dwóch niezależnych wątków, każdy uruchomi funkcję wypisz_wiadomosc */

	tid[0] = pthread_create( &threads[0], NULL, wypisz_wiadomosc, (void*) wiadomosc1);
	tid[1] = pthread_create( &threads[1], NULL, wypisz_wiadomosc, (void*) wiadomosc2);

	/* Funkcja main musi poczekać na zakończenie obu wątków, po to by nie powstały procesy Zombie */

	pthread_join( threads[0], NULL);
	pthread_join( threads[1], NULL);

	printf("Wątek 1 zwraca: %d\n",tid[0]);
	printf("Wątek 2 zwraca: %d\n",tid[1]);
	exit(0);
	
	while(1) {
		
		int addrlen=sizeof(struct sockaddr);
		socket_client = accept(socket_server,(struct sockaddr*)&client_addr,&addrlen);
		if(socket_client<0) continue;
		pthread_t pth;
		pthread_create(&pth,NULL,(void*)wyslij_wiadomosc,(void*) &socket_client);
	}
}

void *wyslij_wiadomosc(void* socket_client){
	char bufor[1024];
	int socket = *(int*)socket_client;
	sprintf(bufor,"Hello world.\n");
	write(socket,bufor,1024);
}

