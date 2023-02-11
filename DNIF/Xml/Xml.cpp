#include <string>
#include <fstream>
#include <vector>

using namespace std;

struct Osoba
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
    OutFile.open("Nif.xml", ios_base::out);

    unsigned int i = 0;
    OutFile << "<?xml version=\"1.0\" encoding=\"ISO-8859-2\"?>" << endl;
    OutFile << "<czlowiek>\n";

    while(i < o.size() - 2)
    {
    	OutFile << "<osoba>\n<imie>" << o[i].Imie << "</imie><nazwisko>" << o[i].Nazwisko << "</nazwisko><urodziny>" << o[i].Urodziny << "</urodziny><email>" << o[i].Email << "</email><wzrost>" << o[i].Wzrost << "</wzrost><numer1>" << o[i].Numer1 << "</numer1><numer2>" << o[i].Numer2 << "</numer2><numer3>" << o[i].Numer3 << "</numer3><plec>" << o[i].Plec << "</plec>\n</osoba>";
	   	i++;

    }
    OutFile << "</czlowiek>";
    return 0;
}
