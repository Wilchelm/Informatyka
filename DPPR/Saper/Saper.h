#ifndef Saper.h
#define Saper.h

int ry, rx; // ry - rozmiar na osi y (liczba wierszy), rx - rozmiar na osi x (liczba kolumn)
int liczba_min; // zawiera informacje o liczbie min na planszy
int liczba_flag;
char **tab0; // tablica ukryta zawierajaca bomby itd
char **tab1; // tablica ktora widzi gracz
static long czas_gry;
static long czas_gry2;
static long czas_gry3;
static int liczba_odsloniec; // zawiera info ile razy wcisnieto spacje aby odslonic pole
	


void clear_screen();
void menu_drugie(int parametr);
void menu_glowne(int i = 0);
void run_game(int komunikat = 0);
void odslon_pola_wokol(int zi, int zx);


#endif
