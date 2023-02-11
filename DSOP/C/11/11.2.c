#include <unistd.h>
#include <stdio.h>

int systemx(char * program /*lub char program [] */){
    int pid;
    if((pid = fork()) >= 0){
        if(pid == 0){
            execl(program, program , 0);
            exit (1);
        } else {
            int zwrot;
            wait(&zwrot);
            return zwrot;
        }
    } else {
            return -1;
    }
}
