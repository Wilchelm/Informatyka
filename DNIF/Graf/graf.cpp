#include <string>
#include <fstream>
#include <vector>

using namespace std;

struct Graf
{
	int etykieta;
	int x;
	int y;

};

struct Linie
{
	int linia1;
	int linia2;
};

int main()
{
    int liczba;
    int ilosc;

    fstream InFile;
    InFile.open("graf.txt", ios_base::in);


    vector <Graf> g;         //wezly
    vector <Linie> l;                //krawedzie

    if(InFile.is_open())
    {
        InFile >> liczba >> ilosc;

        for(int i = 0; i < liczba; i++)
        {
            Graf a;
            InFile >> a.etykieta >> a.x >> a.y;

            g.push_back(a);
            //File << "%! /x a.x def /y a.y def newpath x y moveto lineto closepath stroke showpage";
        }

        for(int i = 0; i < ilosc; i++)
        {
            Linie b;
            InFile >> b.linia1 >> b.linia2;
            l.push_back(b);
        }
        InFile.close();
    }
	
    fstream OutFile;
    OutFile.open("graf.eps", ios_base::out);
	if(OutFile.is_open())
	    {
	        OutFile << "%!PS-Adobe-2.0 EPSF-3.0\n%%BoundingBox: 00 00 700 700\n%%Document-Fonts:Arial\n%%EndComments\n/Arial findfont\n22 scalefont\nsetfont\n%%Page: 1 1\nsave\n0.8000 0.0000 0.0000 setrgbcolor\n";
	        for(int i = 0; i < l.size(); i++)
	        {
	            int t;
	            t = l[i].linia1 - 1;     //bo numerowanie zaczyna sie od 0
	            OutFile << "newpath\n" << g[t].x << " " << g[t].y << " moveto\n";
	
	            t = l[i].linia2 - 1;
	            OutFile << g[t].x << " " << g[t].y << " lineto\nstroke\n";
	        }
	        
	        OutFile << "0.0000 0.9000 0.0000 setrgbcolor\n";

	        for(int i = 0; i < liczba; i++)
	        {
	            OutFile << "newpath\n" << g[i].x << " " << g[i].y << " 18 0 360 arc closepath fill\n";
	        }
	
	        OutFile << "0.0000 0.8900 0.8900 setrgbcolor\n";
	
	        for(int i = 0; i < liczba; i++)
	        {
	            OutFile << "newpath\n" << g[i].x << " " << g[i].y << " 15 0 360 arc closepath fill\n";
	        }
	
	        OutFile << "0.0000 0.0000 0.0000 setrgbcolor\n";
	
	        for(int i = 0; i < liczba; i++)                 //ustawienie etykiet
	        {
	            OutFile << "newpath\n" << g[i].x - 6 << " " << g[i].y - 6 << " moveto\n(" << g[i].etykieta << ") show\n";
	        }
	
			OutFile << "restore";
	        OutFile.close();
	    }
    return 0;
}
