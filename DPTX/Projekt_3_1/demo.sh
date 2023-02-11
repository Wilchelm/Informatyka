#!/bin/sh
bison -d mjog.y
flex mjog.l
gcc -w lex.yy.c mjog.tab.c -lfl
cat example | ./a.out > wy
dot -Tpng wy -o a.png
dot -Tps wy -o a.eps
dot -Tjpg wy -o a.jpg
dot -Tgif wy -o a.gif
