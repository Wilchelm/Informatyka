#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>

#define BUFSIZ 5

int main(){
    char t[BUFSIZ];
    int f = open("plik.txt", O_RDWR);
    read(f, t, BUFSIZ);
    write(f, "X", 1);
    return 0;
}
