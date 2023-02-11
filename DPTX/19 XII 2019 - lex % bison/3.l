%{

   #include <stdio.h>
   #include "3.tab.h"

%}

%%

0|1     return CYFRA;
,       return ',';
"("     return '(';
")"     return ')';
" "|"\n" ;
. {printf("Błąd leksykalny.\n"); exit(1);}
