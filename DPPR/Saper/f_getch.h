#include <stdio.h>
#include <unistd.h>
#ifdef _WIN32
#include <conio.h>
#else
#include <termios.h>
 
int getch (void)
{
        int key;
        struct termios oldSettings, newSettings;    /* stuktury z ustawieniami terminala */
 
        tcgetattr(STDIN_FILENO, &oldSettings);    /* pobranie ustawien terminala */
        newSettings = oldSettings;
        newSettings.c_lflag &= ~(ICANON | ECHO);    /* ustawienie odpowiednich flag */
        tcsetattr(STDIN_FILENO, TCSANOW, &newSettings);    /* zastosowanie ustawien */
        key = getchar();    /* pobranie znaku ze standardowego wejscia */
        tcsetattr(STDIN_FILENO, TCSANOW, &oldSettings);    /* przywrocenie poprzednich ustawien terminala */
        return key;
}
#endif
