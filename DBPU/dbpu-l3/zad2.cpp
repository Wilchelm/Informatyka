/* 
Testując zadania z poprzednich ćwiczeń wszystkie z ćwiczeń 1 i 2-gich za pomocą Valgrida otrzymywałem 

All heap blocks were freed -- no leaks are possible
For counts of detected and suppressed errors, rerun with: -v
ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)

Dlatego postanowiłem zrobić zadanie na przykładzie z wykładu.

I tu są następujące błędy:
Invalid free() / delete / delete[] / realloc()
czyli zwalnianie pamięci w nie odpowiedni sposób w stosunku do tego jak alokowaliśmy ją

Mismatched free() / delete / delete []

==9370== LEAK SUMMARY:
==9370==    definitely lost: 8 bytes in 2 blocks
==9370==    indirectly lost: 0 bytes in 0 blocks
==9370==      possibly lost: 0 bytes in 0 blocks
==9370==    still reachable: 0 bytes in 0 blocks
==9370==         suppressed: 0 bytes in 0 blocks

W efekcie utraciliśmy dostęp/wskaźnik do 2 bloków.

*/





#include <iostream>
#include <malloc.h>
using namespace std;

int main(){

    int *abc=new int(10);
    abc+=10;

    int *def=new int(20);
    def=new int(20);

    free(abc);
    delete(abc);
    delete[](def);

}
