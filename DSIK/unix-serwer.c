#include <stdio.h>
#include <stdlib.h>
#include <errno.h>
#include <string.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <sys/un.h>

int main(void)
{
    int s1, s2, t, len;
    struct sockaddr_un server_sock, client_sock;
    char buff[1000];

    if ((s1 = socket(AF_UNIX, SOCK_STREAM, 0)) == -1) {
        perror("socket");
        exit(1);
    }

    server_sock.sun_family = AF_UNIX;
    strcpy(server_sock.sun_path, "/tmp/.mysocket");
    unlink(server_sock.sun_path);
    len = strlen(server_sock.sun_path) + sizeof(server_sock.sun_family);
    if (bind(s1, (struct sockaddr *)&server_sock, len) == -1) {
        perror("bind");
        exit(1);
    }

    if (listen(s1, 5) == -1) {
        perror("listen");
        exit(1);
    }

    for(;;) {
        int done, n;
        printf("Oczekuję na połączenia...\n");
        t = sizeof(client_sock);
        if ((s2 = accept(s1, (struct sockaddr *)&client_sock, &t)) == -1) {
            perror("accept");
            exit(1);
        }

        printf("Otrzymałem połączenie.\n");

        done = 0;
        do {
            n = recv(s2, buff, 100, 0);
            if (n <= 0) {
                if (n < 0) perror("recv");
                done = 1;
            }

            if (!done)
                if (send(s2, buff, n, 0) < 0) {
                    perror("send");
                    done = 1;
                }
        } while (!done);

        close(s1);
        close(s2);
    }

    return 0;
}
