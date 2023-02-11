
%{
   #include "pjp.tab.h"
   #include <stdio.h>
   #include "string.h"
%}

%%

[0-9]+               yylval.i=atoi(yytext); return LICZBA;

jest                 return JEST;
zmienną              return ZMIENNOM;
jeśli                return JESLI;
umieść               return UMIESC;
w                    return W;
dla                  return DLA;
od                   return OD;
do                   return DO;
wykonaj              return WYKONAJ;
dotąd                return DOTAD;
większe              return WIEKSZE;
mniejsze             return MNIEJSZE;
równe                return ROWNE;
to                   return TO;
wpr                  return WPR;
wjeśli               return WJESLI;  
definiuj             return DEFFUNKCJA;
stopdefiniuj         return STOPDEFFUNKCJA;               


[+*/-]               return *yytext;


[a-z]                yylval.c = *yytext; return ZMIENNA;

[A-Z]                yylval.c = *yytext; return STALA;

[a-z]+               strcpy(yylval.s, yytext); return NAZWAFUNKCJI;

pokaż                return POKAZ;

[ \n\t]              ;

.                    printf("BŁĄD LEKSYKALNY!\n"); exit(1);
