#include <stdio.h>
#include <time.h> 

int main()
{
    int nums1[100];
    int nums2[100];
    int nums3[100];

    struct timespec start, stop;
    timespec_get(&start, TIME_UTC);
    char buff1[100], buff2[100];
    strftime(buff1, sizeof buff1, "%D %T", gmtime(&start.tv_sec));

    for (int i = 0; i < 100; i++)
        nums1[i] = i * 2;

    for (int i = 0; i < 100; i++)
        nums2[i] = i * 3;

    for (int i = 0; i < 100; i++) 
        nums3[i] = (nums1[i]*nums2[i])%30;

    timespec_get(&stop, TIME_UTC);
    strftime(buff2, sizeof buff2, "%D %T", gmtime(&stop.tv_sec));

    printf ("Wykonanie w C: %ld nanosekund\n", stop.tv_nsec-start.tv_nsec);
    return 0;
}
