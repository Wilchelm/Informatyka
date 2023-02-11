#ifndef KOMPUTER_H
#define KOMPUTER_H

#include <string>

using namespace std;

class Komputer
{
	public:
		Komputer(string producent, int procesor, int ram):
			producent(producent),
			ram(ram){}
			
			
		string wypisz();
		
	protected:
		string producent;
		
		int procesor; // w Ghz
		int ram; // w GB
};

#endif
