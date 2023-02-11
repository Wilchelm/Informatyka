%{

   #include <stdio.h>
   #include "2.tab.h"

%}

%%

0|1     return CYFRA;
" "|"\n" ;
. {printf("Błąd leksykalny.\n"); exit(1);}
