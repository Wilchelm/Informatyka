#include <string>
#include <fstream>
#include <vector>

using namespace std;

class Osoba
{
	public:
    string Imie;
    string Nazwisko;
    string Urodziny;
    string Email;
    string Wzrost;
    string Numer1;
    string Numer2;
    string Numer3;
    string Plec;
};

int main()
{
    fstream InFile;
    InFile.open("dane.txt", ios_base::in);

    vector<Osoba> o;
    while(!InFile.eof())
    {
        Osoba a;
        InFile >> a.Imie >> a.Nazwisko >> a.Urodziny >> a.Email >> a.Wzrost >> a.Numer1 >> a.Numer2 >> a.Numer3 >> a.Plec;
        o.push_back(a);
    }
    fstream OutFile;
    OutFile.open("Nif.rtf", ios_base::out);

    unsigned int i = 0;
    OutFile << "{\\rtf1\\ansicpg1250\n{\\fonttbl{\\f0\\fcharset1250 Times New Roman;}{\\f1\\fcharset1250 Calibri;}{\\f2\\fcharset1250 Tahoma}}\n{\\colortbl;\\red0\\green0\\blue0;\\red250\\green0\\blue;\\red13\\green1\\blue80;}\n" << endl;

    while(i < o.size() - 2)
    {
        OutFile << "\\trowd\n\\trqc\n";
        OutFile << "\\clbrdrt\\brdrs\\clbrdrl\\brdrs\\clbrdrb\\brdrs\\clbrdrr\\brdrs\n\\cellx5000\n\\clbrdrt\\brdrs\\clbrdrl\\brdrs\\clbrdrb\\brdrs\\clbrdrr\\brdrs\n\\cellx10000\n";
        OutFile << "\\chshdng1\\chcbpat0\n\\cf2\\fs24\\f1\\qc " << o[i].Imie << " " << o[i].Nazwisko << "\\intbl\\par\n\\ql " << o[i].Urodziny << "\\intbl\\par\n" << o[i].Email << "\\intbl\\par\n" << o[i].Wzrost << "\\intbl\\par\n" << o[i].Numer1 << "\\intbl\\par\n" << o[i].Numer2 << "\\intbl\\par\n" << o[i].Numer3 << "\\intbl\\par\n" << o[i].Plec << "\\intbl\\cell\n";
        OutFile << "\\chshdng0\\chcbpat3\n\\fs30\\f2\\qr " << o[i+1].Imie << " " << o[i+1].Nazwisko << "\\intbl\\par\n\\ql " << o[i+1].Urodziny << "\\intbl\\par\n" << o[i+1].Email << "\\intbl\\par\n" << o[i+1].Wzrost << "\\intbl\\par\n" << o[i+1].Numer1 << "\\intbl\\par\n" << o[i+1].Numer2 << "\\intbl\\par\n" << o[i+1].Numer3 << "\\intbl\\par\n" << o[i+1].Plec << "\\intbl\\cell\n\\row\n";
        i += 2;
    }
    OutFile << "}";
    return 0;
}
