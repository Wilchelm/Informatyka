#include <iostream>

using namespace std;

#ifdef _WIN32
#include <windows.h>
#endif

ostream &red(ostream& os) {
#ifdef __gnu_linux__
    return os << "\033[31m";
#elif defined _WIN32
    os.flush();
    HANDLE console;
    console = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(console, 4);
    return os;
#endif
}

ostream &reset(ostream& os) {
#ifdef __gnu_linux__
    return os << "\033[0m";
#elif defined _WIN32
    os.flush();
    HANDLE console;
    console = GetStdHandle(STD_OUTPUT_HANDLE);
    SetConsoleTextAttribute(console, 7);
    return os;
#endif
}
