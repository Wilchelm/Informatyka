#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>

int main( void )
{
    int c;
    size_t n;
    char *word;
    char *tmp;
    char string[40] = {"\0"} ;

    n = 0;
    word = malloc( n + 1 );
    word[n++] = '\0';

    printf( "Wpisz wyraz: " );

    while ( ( c = getchar() ) != EOF && !isspace( c ) && ( tmp = realloc( word, n + 1 ) ) != NULL )
    {
        word = tmp;
        word[n-1] = c;
        word[n++] = '\0';
    }

    //int a = 10, b = 20, c; 
    //c = a + b; 
    // Przepisywanie wielu zmiennych do jednej
    //sprintf(string, "Suma %d i %d wynosi %d", a, b, c); 
 
    sprintf( string, "podano: \"%s\"\n", word );
    printf("%s", string);

    free( word );
}  
