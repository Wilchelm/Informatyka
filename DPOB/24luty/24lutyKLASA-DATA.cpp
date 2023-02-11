#include<iostream>
#include<ctime>
#include <cstdio>
#include "klasa_data.h"
using namespace std;

int main(){
	Data data;
	data.set(10,5,1995);
    data.print();
    Data data2(4,5,1990);
    data2.print();
}
