#include "./main.h"

using namespace std;

int main()
{
	CPrinter::setDebugLevel(4);
	MSG_PRINT("Ala ma kota");
    printMessage("Hello makefiles");
    return 0;
}
