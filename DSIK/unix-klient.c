#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>
#include <sys/time.h>

#define ATTEMPTS 100

int main(void)
{
    int s1, n, len;
    struct sockaddr_un server_socket;
    char buff[1000];
    struct timeval time_b, time_e;

    if ((s1 = socket(AF_UNIX, SOCK_STREAM, 0)) == -1) {
        perror("socket");
        exit(1);
    }

    printf("Trying to connect...\n");

    server_socket.sun_family = AF_UNIX;
    strcpy(server_socket.sun_path, "/tmp/.mysocket");
    len = strlen(server_socket.sun_path) + sizeof(server_socket.sun_family);
    if (connect(s1, (struct sockaddr *)&server_socket, len) == -1) {
        perror("connect");
        exit(1);
    }

    printf("Connected.\n");

    while(printf("> "), fgets(buff, 100, stdin), !feof(stdin)) {
        gettimeofday(&time_b, NULL);
        if (send(s1, buff, strlen(buff), 0) == -1) {
            perror("send");
            exit(1);
        }

        if ((n=recv(s1, buff, 100, 0)) > 0) {
            buff[n] = '\0';
            printf("%s", buff);

            gettimeofday(&time_e, NULL);

        printf("czas: %.6f s\n",(((double) (time_e.tv_sec - time_b.tv_sec) * 1000000) +((double) (time_e.tv_usec - time_b.tv_usec)))/ (1000000.0 * ATTEMPTS));

        } else {
            if (len < 0) perror("recv");
            else printf("Serwer zamknął połączenie\n");
            exit(1);
        }
    }

    close(s1);

    return 0;
}
