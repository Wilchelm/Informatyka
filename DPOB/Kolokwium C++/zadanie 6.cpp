#include <iostream>
#include <string>>
Nusing namespace std;

class Stos
{
private:
  int dane[100];
  int n;
public:
  void init()        { n=0; }
  void push(int e)   { dane[n++] = e; }
  int  pop()         { return dane[--n]; }
  int  empty()       { return n==0; }
};

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
	return 0;
}
