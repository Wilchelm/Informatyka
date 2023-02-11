#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>

int main(int argc, char **argv)
{
    int fd2 = open("./test.svg", O_RDWR|O_CREAT, 0600);  

    if (fd2 != -1) {
        close(fd2);
    }

    return(0);
}
