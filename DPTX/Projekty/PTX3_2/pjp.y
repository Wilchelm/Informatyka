%{
    char text[100];
    char text2[100];
    char text3[100];
    char text4[100];
    int digit=0;
    #include <stdio.h>
    int yyerror(char*);
    int yylex();
%}



%token <i> LICZBA
%token JESLI
%token UMIESC
%token W
%token <c> ZMIENNA
%token <i> STALA
%token POKAZ
%token JEST
%token ZMIENNOM
%token DLA
%token OD
%token DO
%token WYKONAJ
%token DOTAD
%token WIEKSZE
%token ROWNE
%token MNIEJSZE
%token TO
%token WPR
%token WJESLI
%token DEFFUNKCJA
%token STOPDEFFUNKCJA
%token <s> NAZWAFUNKCJI

%left '+' '-'
%left '*' '/'

%union { char s[100]; int i; char c; }

%%


program : { 
            printf(".sub main\n");
	    printf(".local pmc stos\n");
            printf("    stos = new 'ResizableFloatArray'\n");
            printf(".local num tmp\n");
            printf(".local num tmp2\n");
            printf(".local num tmp3\n");
	  }
          instrukcje
          { printf(".end\n"); }
          funkcje
          ;

funkcje : funkcja
        | funkcja funkcje
        |
        ;

funkcja : DEFFUNKCJA NAZWAFUNKCJI     {
                                        printf("\n.sub %s\n", $2); 
	                                printf(".local pmc stos\n");
                                        printf("    stos = new 'ResizableFloatArray'\n");
                                        printf(".local num tmp\n");
                                        printf(".local num tmp2\n");
                                        printf(".local num tmp3\n");
                                      }
          instrukcje
          STOPDEFFUNKCJA { printf(".end\n"); }
         ;
        

instrukcje : instrukcja
           | instrukcja instrukcje
           ;

instrukcja : przypisanie
           | deklaracja_zmiennej
           | drukowanie
           | petladla
           | jesli
           | wpr
           | wywolaj
           ;

wywolaj : NAZWAFUNKCJI  { printf("%s()\n", $1); } ;

deklaracja_zmiennej : ZMIENNA JEST ZMIENNOM { printf(".local num %c\n", $1); } ;

przypisanie : UMIESC wyrazenie W ZMIENNA { printf("pop tmp,stos\n%c = tmp\n",$4); } ;

drukowanie : POKAZ wyrazenie {printf("pop tmp,stos\nsay tmp\n");} ;

petladla : DLA
           ZMIENNA
           OD
           wyrazenie
           {
             printf("pop tmp,stos\n%c = tmp\nBEGINLOOP:\n",$2);
           }
           DO
           wyrazenie
           { 
             printf("pop tmp,stos\n");
             printf("if %c > tmp goto ENDLOOP\n",$2); 
           }
           WYKONAJ
           instrukcje
           DOTAD
           {
             printf("inc %c\n",$2);
             printf("goto BEGINLOOP\n");
             printf("ENDLOOP:\n");
           }
           ;


wyrazenie : LICZBA { printf("push stos,%d.0\n",$1); }
          | STALA
          | ZMIENNA { printf("push stos,%c\n",$1); }
          | wyrazenie '+' wyrazenie   { printf("pop tmp2,stos\npop tmp3,stos\n tmp=tmp2+tmp3\n push stos,tmp\n"); }
          | wyrazenie '-' wyrazenie   { printf("pop tmp2,stos\npop tmp3,stos\n tmp=tmp3-tmp2\n push stos,tmp\n"); }
          | wyrazenie '*' wyrazenie   { printf("pop tmp2,stos\npop tmp3,stos\n tmp=tmp2*tmp3\n push stos,tmp\n"); }
          | wyrazenie '/' wyrazenie   { printf("pop tmp2,stos\npop tmp3,stos\n tmp=tmp3/tmp2\n push stos,tmp\n"); }
          ;
opera : MNIEJSZE        { printf(" < "); } 
      | WIEKSZE         { printf(" > "); }
      | ROWNE           { printf(" == "); }
      | WIEKSZE ROWNE   { printf(" >= "); }
      | MNIEJSZE ROWNE  { printf(" <= "); }
      ;

cos : ZMIENNA  { printf("%c", $1); }
    | LICZBA   { printf("%d", $1); }
    ;

jesli : JESLI  { printf("if "); }
        cos
        opera 
        cos
        TO        { 
                    sprintf(text, "ETYKIETA%d", digit);
                    sprintf(text2, "ETYKIETA%d:", digit);
                    printf(" goto %s\n", text);
                    digit = digit + 1;
                    printf("%s\n", text2);
                  }
        instrukcje
        ;

wpr : WJESLI  { printf("if "); }
      cos
      opera 
      cos
      TO        { 
                  sprintf(text, "ETYKIETA%d", digit);
                  sprintf(text2, "ETYKIETA%d:", digit);
                  printf(" goto %s\n", text);
                  digit = digit + 1;
                  sprintf(text3, "ETYKIETA%d", digit);
                  sprintf(text4, "ETYKIETA%d:", digit);
                  printf("goto %s\n", text3);
                  digit = digit + 1;
                  printf("%s\n", text2);
                }
      instrukcje
      WPR
                {
                  printf("%s\n", text4);
                }
      instrukcje
      ;

%%

int main() { 
            yyparse(); 
}

int yyerror(char* s) { printf("B????D SK??ADNIOWY!\n"); }
