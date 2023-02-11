#include <unistd.h>
#include <stdio.h>

int main(){
    execl("/bin/sleep", "sleep", "5", (char *)0);
    printf("Czy ten napis sie wyswietli?");
    return 0;
}
