%{

   #include <stdio.h>
   int yyerror(char*);
   int yylex();

%}

%token CYFRA

%%

wyr : '(' ciag ')'
    ;

ciag : CYFRA
     | ciag ',' CYFRA
     ;

%%

int yyerror(char* s) { printf("%s\n",s); }

int main() { yyparse(); }
