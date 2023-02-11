#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
int main(){
int pid;
if((pid = fork()) >= 0){
if(pid == 0){
printf("Dziecko - PPID: %d\n, PID: %d",getppid(), getpid());
} else {
printf("Rodzic - PPID: %d, PID: %d, CPID: %d\n",getppid(), getpid(), pid);
}
} else {
perror("fork");
}
return 0;
}
