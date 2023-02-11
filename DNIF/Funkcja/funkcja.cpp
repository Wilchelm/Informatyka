#include <iostream>
#include <vector>
#include <fstream>
#include <math.h>
using namespace std;

int main(){
	vector < double > dane;
	double result;
	for(int x=-100 ; x<100; x++)
	{
		result = x;
		dane.push_back(result);
		
	}
	
	
	fstream OutFile;
    OutFile.open("funkcja.eps", ios_base::out);
	if(OutFile.is_open())
	    {
	        OutFile << "%!PS-Adobe-2.0 EPSF-3.0\n%%BoundingBox: 00 00 201 201\n%%Document-Fonts:Arial\n%%EndComments\n/Arial findfont\n8 scalefont\nsetfont\n%%Page: 1 1\nsave\n0.0000 0.0000 0.0000 setrgbcolor\n";
	        
	        OutFile << "newpath\n" << "101" << " " << "0" << " moveto\n";
			OutFile << "101" << " " << "201" << " lineto stroke\n";
	        OutFile << "newpath\n" << "0" << " " << "101" << " moveto\n";
	        OutFile << "201" << " " << "101" << " lineto stroke\n";
	        OutFile << "newpath\n" << "111" << " " << "99" << " moveto\n";
			OutFile << "111" << " " << "103" << " lineto stroke\n";
	        OutFile << "newpath\n" << "99" << " " << "111" << " moveto\n";
			OutFile << "103" << " " << "111" << " lineto stroke\n";
			OutFile << "newpath\n" << "109" << " " << "92" << " moveto\n" << "(1)" << " show\n";
			OutFile << "newpath\n" << "94" << " " << "109" << " moveto\n" << "(1)" << " show\n";
			OutFile << "newpath\n" << "196" << " " << "103" << " moveto\n";
			OutFile << "201" << " " << "101" << " lineto stroke\n";
			OutFile << "newpath\n" << "196" << " " << "99" << " moveto\n";
			OutFile << "201" << " " << "101" << " lineto stroke\n";
			OutFile << "newpath\n" << "103" << " " << "196" << " moveto\n";
			OutFile << "101" << " " << "201" << " lineto stroke\n";
			OutFile << "newpath\n" << "99" << " " << "196" << " moveto\n";
			OutFile << "101" << " " << "201" << " lineto stroke\n";
			OutFile << "0.8000 0.0000 0.0000 setrgbcolor\n" << "/function {\n" << "1.0000 setlinewidth\n";
	
			OutFile << "newpath\n" << "0" << " " << "0" << " moveto\n";
			for(int i=0; i<dane.size(); i++)
				OutFile << i << " " << dane[i] << " lineto\n";
	
			OutFile << "} def\n" << "1 1 scale\n" << "function 0 101 translate\n"<< "function stroke\n";OutFile.close();
	    }
    return 0;
}

