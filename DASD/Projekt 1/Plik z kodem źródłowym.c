#include <stdio.h>

void metoda1() {
int a,b;
scanf ("%d %d", &a, &b);
a=a+b;
b=a-b;
a=a-b;
printf("%d %d", a, b);
}


void metoda2() {
int a,b;
scanf ("%d %d", &a, &b);
b=a+b;
a=b-a;
b=b-a;
printf("%d %d", a, b);
}


void metoda3() {
int a,b;
scanf ("%d %d", &a, &b);
if(a != 0 && b != 0) {
  a=a*b;
  b=a/b;
  a=a/b;
  printf("%d %d", a, b);
}
}


void metoda4() {
int a,b;
scanf ("%d %d", &a, &b);
if(a != 0 && b != 0) {
  b=a*b;
  a=b/a;
  b=b/a;
  printf("%d %d", a, b);
}
}


void metoda5() {
int a,b;
scanf ("%d %d", &a, &b);
a = a + b - (b = a);
printf("%d %d", a, b);
}


void metoda6() {
int a,b;
scanf ("%d %d", &a, &b);
b = a + b - (a = b);
printf("%d %d", a, b);
}


void metoda7() {
int a,b;
scanf ("%d %d", &a, &b);
a = a^b;
b = a^b;
a = a^b;
printf("%d %d", a, b);
}


void metoda8() {
int a,b;
scanf ("%d %d", &a, &b);
b = a^b;
a = a^b;
b = a^b;
printf("%d %d", a, b);
}


void metoda9() {
int a,b;
scanf ("%d %d", &a, &b);
a=a-b;
b=a+b;
a=b-a;
printf("%d %d", a, b);
}


void metoda10() {
int a,b;
scanf ("%d %d", &a, &b);
b=b-a;
a=a+b;
b=a-b;
printf("%d %d", a, b);
}

void main()
{
metoda1();
metoda2();
metoda3();
metoda4();
metoda5();
metoda6();
metoda7();
metoda8();
metoda9();
metoda10();
}
