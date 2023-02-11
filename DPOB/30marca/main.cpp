#include <iostream>

#include "lista.h"
#include "lista.cpp"

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int main(int argc, char** argv) {
        Lista<int> lista;
        lista.wstawElement(5);
        lista.wstawElement(15);
        lista.wstawElement(25);
        lista.wstawElement(7);
        
        std::cout << lista.podajElement(2) << std::endl;
        return 0;
        
}
