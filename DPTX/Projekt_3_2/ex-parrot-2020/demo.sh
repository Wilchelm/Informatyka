#!/bin/sh
bison -d pjp.y
flex pjp.l
gcc -w lex.yy.c pjp.tab.c -lfl
./a.out | parrot -


