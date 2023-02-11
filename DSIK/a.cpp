#include <stdio.h>
#include <stdlib.h>

#include <netdb.h>
#include <netinet/in.h>

#include <string.h>

int main(int argc, char *argv[]) {
        char abcd[512];
        int sockfd, portno, n;
        struct sockaddr_in serv_addr;
        struct hostent *server;

        char buffer[256];

        printf("Podaj adres IP odbiorcy: ");
        scanf("%s", abcd);
        printf("Podaj numer portu odbiorcy: ");
        scanf("%u", &portno);

        /* Create a socket point */
        sockfd = socket(AF_INET, SOCK_STREAM, 0);

        if (sockfd < 0) {
                perror("ERROR opening socket");
                exit(1);
        }

        serv_addr.sin_family = AF_INET;
        serv_addr.sin_port = htons(portno);
        serv_addr.sin_addr.s_addr = inet_addr(abcd);

        /* Now connect to the server */
        if (connect(sockfd, (struct sockaddr*)&serv_addr, sizeof(serv_addr)) < 0) {
                perror("ERROR connecting");
                exit(1);
        }

        /* Now ask for a message from the user, this message
                * will be read by server
        */

        printf("Please enter the message: ");
        bzero(buffer,256);
        scanf("%s", buffer);

        /* Send message to the server */
        n = write(sockfd, buffer, strlen(buffer));

        if (n < 0) {
                perror("ERROR writing to socket");
                exit(1);
        }

        /* Now read server response */
        bzero(buffer,256);
        n = read(sockfd, buffer, 255);

        if (n < 0) {
                perror("ERROR reading from socket");
                exit(1);
        }

        printf("%s\n",buffer);
        return 0;
}
