#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>

int system(char* polecenie)
{
int pid;
if((pid=fork())>=0)
{
	if(pid==0)
	{
	execl(polecenie,polecenie, "/");
	exit(1);
	}else{
	int ret=0;
	wait(&ret);
	return ret;
	}
}else{ return -1; }
}

int main()
{
printf("status wyjścia procesu ls:%d",system("/bin/ls"));
return 0;
}
