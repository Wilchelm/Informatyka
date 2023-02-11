#include<iostream>  
  
using namespace std; 
  

/*

Zawsze wyszło mi tak samo, a mam odwrócona kolejność pętli, oraz odwróconą kolejność w pętli tj. iteracje 0->99 i 99->0



--10802-- warning: L3 cache found, using its data for the LL simulation.
==10802== 
==10802== I   refs:      2,404,949
==10802== I1  misses:        1,596
==10802== LLi misses:        1,535
==10802== I1  miss rate:      0.07%
==10802== LLi miss rate:      0.06%
==10802== 
==10802== D   refs:        779,553  (609,348 rd   + 170,205 wr)
==10802== D1  misses:       16,609  ( 13,699 rd   +   2,910 wr)
==10802== LLd misses:        9,919  (  7,904 rd   +   2,015 wr)
==10802== D1  miss rate:       2.1% (    2.2%     +     1.7%  )
==10802== LLd miss rate:       1.3% (    1.3%     +     1.2%  )
==10802== 
==10802== LL refs:          18,205  ( 15,295 rd   +   2,910 wr)
==10802== LL misses:        11,454  (  9,439 rd   +   2,015 wr)
==10802== LL miss rate:        0.4% (    0.3%     +     1.2%  )

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

int main() 
{ 
int a[100], b[100], c[100][100];
for (int i = 0; i < 100; i++) {a[i]=i; b[i]=i;}


for (int i = 0; i < 100; i++) {
    for (int j = 0; j < 100; j++) {
        c[i][j]=a[i]*b[j];
    }
}

      
    return 0; 
} 

==10859== I   refs:      2,404,949
==10859== I1  misses:        1,596
==10859== LLi misses:        1,535
==10859== I1  miss rate:      0.07%
==10859== LLi miss rate:      0.06%
==10859== 
==10859== D   refs:        779,553  (609,348 rd   + 170,205 wr)
==10859== D1  misses:       16,668  ( 13,701 rd   +   2,967 wr)
==10859== LLd misses:        9,919  (  7,904 rd   +   2,015 wr)
==10859== D1  miss rate:       2.1% (    2.2%     +     1.7%  )
==10859== LLd miss rate:       1.3% (    1.3%     +     1.2%  )
==10859== 
==10859== LL refs:          18,264  ( 15,297 rd   +   2,967 wr)
==10859== LL misses:        11,454  (  9,439 rd   +   2,015 wr)
==10859== LL miss rate:        0.4% (    0.3%     +     1.2%  )

^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



int main() 
{ 
int a[100], b[100], c[100][100];
for (int i = 0; i < 100; i++) {a[i]=i; b[i]=i;}


for (int j = 0; j < 100; j++) {
    for (int i = 0; i < 100; i++) {
        c[i][j]=a[i]*b[j];
    }
}

      
    return 0; 
}

==12017== I   refs:      2,404,949
==12017== I1  misses:        1,596
==12017== LLi misses:        1,535
==12017== I1  miss rate:      0.07%
==12017== LLi miss rate:      0.06%
==12017== 
==12017== D   refs:        779,553  (609,348 rd   + 170,205 wr)
==12017== D1  misses:       16,667  ( 13,700 rd   +   2,967 wr)
==12017== LLd misses:        9,919  (  7,904 rd   +   2,015 wr)
==12017== D1  miss rate:       2.1% (    2.2%     +     1.7%  )
==12017== LLd miss rate:       1.3% (    1.3%     +     1.2%  )
==12017== 
==12017== LL refs:          18,263  ( 15,296 rd   +   2,967 wr)
==12017== LL misses:        11,454  (  9,439 rd   +   2,015 wr)
==12017== LL miss rate:        0.4% (    0.3%     +     1.2%  )


^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

*/
int main() 
{ 
int a[100], b[100], c[100][100];
for (int i = 0; i < 100; i++) {a[i]=i; b[i]=i;}


for (int j = 99; j >= 0; j--) {
    for (int i = 99; i >= 0; i--) {
        c[i][j]=a[i]*b[j];
    }
}

      
    return 0; 
}








