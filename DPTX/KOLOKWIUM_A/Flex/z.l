%{

   #include <stdio.h>
   #include "z.tab.h"

%}

%%

0|1     	return CYFRA;
"("     	return '(';
")"     	return ')';

" "|"\n"|"\t"	;
. 		{printf("Błąd leksykalny.\n"); exit(1);}
