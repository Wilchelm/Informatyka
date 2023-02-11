/*
gcc -o nothread.out -Wall zad3.c -lpthread
time ./nothread.out 

real	0m0,026s
user	0m0,026s
sys	0m0,000s

#include <stdio.h>
#include <pthread.h>                             
pthread_mutex_t mut = PTHREAD_MUTEX_INITIALIZER; 
long var = 0;


int main ( void ) {

  while (var<10000000) var++;

  return 0;
}



gcc -o unlocked.out -Wall zad3.c -lpthread
time ./unlocked.out 

real	0m0,033s
user	0m0,033s
sys	0m0,000s


#include <stdio.h>
#include <pthread.h>                             
pthread_mutex_t mut = PTHREAD_MUTEX_INITIALIZER; 
long var = 0;

void* child_fn ( void* arg ) {
  //pthread_mutex_lock(&mut);
  var++;
  pthread_mutex_unlock(&mut);                  
  return NULL;
}

int main ( void ) {

  pthread_t child;
  pthread_create(&child, NULL, child_fn, NULL);
  //pthread_mutex_lock(&mut);                     
  while (var<10000000) var++;
  pthread_mutex_unlock(&mut);                 
  pthread_join(child, NULL);
  

  return 0;
}


gcc -o locked.out -Wall zad3.c -lpthread
time ./locked.out 

real	0m0,034s
user	0m0,035s
sys	0m0,000s


*/

#include <stdio.h>
#include <pthread.h>                             
pthread_mutex_t mut = PTHREAD_MUTEX_INITIALIZER; 
long var = 0;

void* child_fn ( void* arg ) {
  pthread_mutex_lock(&mut);
  var++;
  //pthread_mutex_unlock(&mut);                  
  return NULL;
}

int main ( void ) {

  pthread_t child;
  pthread_create(&child, NULL, child_fn, NULL);
  pthread_mutex_lock(&mut);                     
  while (var<10000000) var++;
  pthread_mutex_unlock(&mut);                 
  pthread_join(child, NULL);
  

  return 0;
}

