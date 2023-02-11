#include <unistd.h>     /* Support all standards    */
#include <sys/mman.h>   /* Memory locking functions */

#define DATA_SIZE 2048

lock_memory(char   *addr,
            size_t  size)
{
  unsigned long    page_offset, page_size;

  page_size = sysconf(_SC_PAGE_SIZE);
  page_offset = (unsigned long) addr % page_size;

  addr -= page_offset;  /* Adjust addr to page boundary */
  size += page_offset;  /* Adjust size with page_offset */

  return ( mlock(addr, size) );  /* Lock the memory */
}

unlock_memory(char   *addr,
              size_t  size)
{
  unsigned long    page_offset, page_size;

  page_size = sysconf(_SC_PAGE_SIZE);
  page_offset = (unsigned long) addr % page_size;

  addr -= page_offset;  /* Adjust addr to page boundary */
  size += page_offset;  /* Adjust size with page_offset */

  return ( munlock(addr, size) );  /* Unlock the memory */
}

main()
{
  //char data[DATA_SIZE];
  char preKey[16];

  //if ( lock_memory(data, DATA_SIZE) == -1 )
  //  perror("lock_memory");

           /* Do work here */
  if ( lock_memory(preKey, 16) == -1 )
    perror("lock_memory");

  for (int i=0; i<16; i++)
  {
    preKey[i]=rand();
    printf("%d\n",preKey[i]);
  }

  if ( unlock_memory(preKey, 16) == -1 )
    perror("unlock_memory");
  //if ( unlock_memory(data, DATA_SIZE) == -1 )
  //  perror("unlock_memory");
/*
valgrind --leak-check=full ./a.out

==16166== HEAP SUMMARY:
==16166==     in use at exit: 0 bytes in 0 blocks
==16166==   total heap usage: 1 allocs, 1 frees, 1,024 bytes allocated
==16166== 
==16166== All heap blocks were freed -- no leaks are possible
==16166== 
==16166== For counts of detected and suppressed errors, rerun with: -v
==16166== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 0 from 0)
*/
}
