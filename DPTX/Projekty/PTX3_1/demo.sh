#!/bin/sh
echo 'Processing: example'
bison -d mjog.y
echo '.'
flex mjog.l
echo '.'
gcc -w lex.yy.c mjog.tab.c -lfl
echo '.'
cat example | ./a.out > wy
echo '.'
echo 'Creating a.png'
dot -Tpng wy -o a.png
echo 'Creating a.jpg'
#dot -Tps wy -o a.eps
dot -Tjpg wy -o a.jpg
echo 'Creating a.gif'
dot -Tgif wy -o a.gif
