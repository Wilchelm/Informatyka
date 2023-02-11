#include <iostream>
#include "stos.h"

main()
{
  Stos *stos = new Stos();
  stos->init();
  stos->push(2); stos->push(5); stos->push(3);
  while(!stos->empty())
  	std::cout << stos->pop() << std::endl;
	
  delete stos;
}

