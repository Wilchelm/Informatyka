%{

   #include <stdio.h>
   #include "mjog.tab.h"
   #include "string.h"

%}

%%

#.*\n         ;
v             return VERTEX;
e             return EDGE;
\"[^"]*\"     strcpy(yylval.s, yytext); return STRING;
[0-9a-zA-Z_]+ strcpy(yylval.s, yytext); return NAME;

[ \t\n]       ;

.             fprintf(stderr,"BŁĄD LEKSYKALNY\n"); exit(1);
