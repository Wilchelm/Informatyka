#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define BUFFER_SIZE 1000

int main()
{
    FILE *fptr;
    char path[100];
    char word[50];
    char str[BUFFER_SIZE];
    char *pos;

    printf("Enter file path: ");
    scanf("%s", path);
    printf("Enter word to search in file: ");
    scanf("%s", word);

    fptr = fopen(path, "r");
    if (fptr == NULL)
    {
        printf("File not exist.\n");
        exit(EXIT_FAILURE);
    }

    while ((fgets(str, BUFFER_SIZE, fptr)) != NULL)
    {
        pos = strstr(str, word);

        if (pos != NULL)
        {
            printf("%s", str);
        }
    }
    

    fclose(fptr);
    return 0;
}
