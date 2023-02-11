#include <iostream>

using namespace std;

int main(int argc, char const *argv[])
{
   int *a = new int;
   //a = new int;  //nadpisujemy adres co powoduje definitely lost: 4 bytes in 1 blocks


   for (int i = 0; i < 5; i++)
     cout << a++ << endl;

   a-=5; 
   delete a;
   //delete a;  //Invalid free() / delete / delete[] / realloc()

   return 0;
}
