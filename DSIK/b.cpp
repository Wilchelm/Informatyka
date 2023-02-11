#include <stdio.h>
#include <netinet/in.h>
#include <sys/socket.h>
#include <arpa/inet.h>

int main(void) {
        unsigned long adr;
        unsigned char *jako_bajty =
        (unsigned char *) &adr;
        char *abcd;
        struct in_addr tmp;

        printf("Podaj adres IP jako liczbe dziesietna w formacie sieci: ");
        scanf("%u",&adr);
        printf("Adres (hex): %X\n", adr);

        printf("Adres jako bajty (hex): %X %X %X %X\n",
                jako_bajty[0], jako_bajty[1],jako_bajty[2], jako_bajty[3]);

        printf("Adres jako bajty (dec): %u %u %u %u\n",
                jako_bajty[0], jako_bajty[1], jako_bajty[2], jako_bajty[3]);

        tmp.s_addr = adr;
        abcd = inet_ntoa(tmp);

        printf("Adres w formacie a.b.c.d: %s\n", abcd);

        return 0;
}
