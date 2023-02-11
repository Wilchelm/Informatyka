%{

   #include <stdio.h>
   int licznik_linii=1;
   char* pom;
   FILE *f; 

%}

%x KOMENTARZ
%x NAPIS

%%

"/*" BEGIN(KOMENTARZ);
"//".* ;

"void" printf("SK_VOID		 %s\n",yytext);
"(" printf("NAW_OTW		 %s\n",yytext);
")" printf("NAW_ZAM		 %s\n",yytext);
"{" printf("KLAM_OTW	 %s\n",yytext);
"}" printf("KLAM_ZAM	 %s\n",yytext);
"for" printf("SK_FOR		 %s\n",yytext);
"int" printf("SK_INT		 %s\n",yytext);
"=" printf("OP_PRZYP	 %s\n",yytext);
";" printf("SRED		 %s\n",yytext);
"<=" printf("OP_LEQ		 %s\n",yytext);
"++" printf("OP_INC		 %s\n",yytext);
"\t" ;
" " ;


[a-z]+ printf("ID		 %s\n",yytext);
[0-9]+ printf("STALA_INT	 %s\n",yytext);

"\"".*"\"" printf("STALA_LANC	 %s\n",yytext);

<*>\n licznik_linii++;

<KOMENTARZ>"*/" BEGIN(INITIAL);
<KOMENTARZ>. ;
<KOMENTARZ><<EOF>> fprintf(stderr, "BLAD! niezakonczony komentarz w linii %d.\n",licznik_linii); exit(1);

%%


  int main()
  {
    yyin = fopen("dane.txt","r");
    yylex();
    fclose(yyin);
  }

