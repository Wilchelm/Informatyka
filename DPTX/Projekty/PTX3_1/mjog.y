%{

   #include <stdio.h>
   int yyerror(char*);
   int yylex();

%}

%token VERTEX EDGE
%token <s> NAME STRING

%union { char s[100]; }

%%

graph : { printf("digraph noname {\n"); } vertices edges { printf("}\n"); } ;

vertices :
         | vertices vertex
         ;

vertex : VERTEX NAME STRING STRING STRING { printf("    %s [label=%s, shape=%s, style=%s]\n", $2, $3, $4, $5); } ;

edges :
      | edges edge
      ;

edge: EDGE NAME NAME STRING { printf("    %s -> %s [label=%s]\n", $2, $3, $4); } ;

%%

int yyerror(char* s) { printf("BŁĄD %s\n",s); }

int main() { yyparse(); }
