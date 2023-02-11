#include <stdio.h>
#include <netinet/in.h>

int main(void) {
        long h, n;
        unsigned char *jako_bajty;
        printf("Podaj liczbe calkowita: ");
        scanf("%d",&h);
        printf("Liczba w formacie lokalnym jako hex: %X\n",h);
        jako_bajty = (unsigned char *) &h;
        printf("Liczba w formacie lokalnym jako bajty hex: %X %X %X %X\n",
                jako_bajty[0],jako_bajty[1],jako_bajty[2],jako_bajty[3]);

        n = htonl(h);

        jako_bajty = (unsigned char *) &n;

        printf("Liczba w formacie sieciowym jako bajty: %X %X %X %X\n",
                jako_bajty[0],jako_bajty[1],jako_bajty[2],jako_bajty[3]);

        printf("Liczba w formacie sieciowym jako hex: %X\n", n);

        printf("co daje dziesietnie %u\n", n);
        return 0;
}
