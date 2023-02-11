#ifndef STOS_H
#define STOS_H

#include <iostream>

class Stos
{
private:
  int dane[100];
  int n;
public:
	Stos()
	{
		n=0;
		std::cout << "Pojawiam sie!" << std::endl;
	}
	~Stos()
	{
		std::cout << "Znikam!" <<std::endl;
	}
	
  void init()        { n=0; }
  void push(int e)   { dane[n++] = e; }
  int  pop()         { return dane[--n]; }
  int  empty()       { return n==0; }
  int zwroc()		 { return n;  }
};


#endif
