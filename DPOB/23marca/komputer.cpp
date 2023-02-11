#include "komputer.h"

#include <sstream>

string Komputer::wypisz(){
	stringstream ss;
	ss<<"Producent" << producent << ", procesor: "<<procesor<< ",ram: " <<ram;
}
