#program:
#	gcc main.c hello.c silnia.c -o program
program: main.o hello.o silnia.o
	gcc main.o hello.o silnia.o -o program

main.o: main.c funkcje.h
	gcc -c main.c

hello.o: hello.c
	gcc -c hello.c

silnia.o: silnia.c
	gcc -c silnia.c

clean:
	-rm *.o program
