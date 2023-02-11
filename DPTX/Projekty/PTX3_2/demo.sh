#!/bin/sh
echo 'Processing: example1'
echo ''
bison -d pjp.y
echo '.'
flex pjp.l
echo '.'
gcc -w lex.yy.c pjp.tab.c -lfl
echo '.'
cat example1 | ./a.out > file1.txt
echo '.'
cat file1.txt | parrot -
echo ''
echo 'Processing: example2'
bison -d pjp.y
echo '.'
flex pjp.l
echo '.'
gcc -w lex.yy.c pjp.tab.c -lfl
echo '.'
cat example2 | ./a.out > file2.txt
echo '.'
cat file2.txt | parrot -
echo ''
echo 'Processing: example3'
bison -d pjp.y
echo '.'
flex pjp.l
echo '.'
gcc -w lex.yy.c pjp.tab.c -lfl
echo '.'
cat example3 | ./a.out > file3.txt
echo '.'
cat file3.txt | parrot -

