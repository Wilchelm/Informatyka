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
    InFile.close();
    
    fstream CssFile;
    CssFile.open("css.css", ios_base::out);
	    {
		    CssFile 
			 << ".one { \n"
			 << "text-align: center;\n" 
			 << "color: black;\n" 
			 << "font-weight: 900;\n" 
			 << "font-size: 20px;}\n\n" 
			
			 << ".two {\n" 
			 << "text-align: center;\n" 
			 << "color: red;}\n\n" 
			
			 << ".three {\n" 
			 << "border-collapse: collapse;\n" 
			 << "border: 5px dotted black;\n" 
			 << "margin-left: auto;\n" 
			 << "margin-right: auto;}\n\n" 
			
			 << ".four {\n" 
			 << "text-align: center;\n\n" 
			 << "border: 5px double red;\n" 
			 << "background-color:blue;}\n\n" 
			
			 << ".five {\n" 
			 << "text-align: center;\n" 
			 << "border: 5px double red;\n" 
			 << "background-color:yellow;}\n\n";
			CssFile.close();
		}
    
    fstream OutFile;
    OutFile.open("Nif-Css.html", ios_base::out);

    unsigned int i = 0;
	    OutFile 
		<< "<!DOCTYPE html>\n"
		<< "<html>\n"
		<< "<head><script type=\"text/javascript\" src=\"/176FBE72FF7F400A94ADF0054C37151B/80F2A1D0-8957-BE43-AAC4-93A18B81471A/main.js\" charset=\"UTF-8\"></script>\n"
		<< "<style>\n"
		<< "</style>\n"
		<< "</head>\n"
		<< "<link rel=\"stylesheet\" type=\"text/css\" href=\"css.css\">\n\n"
		<< "<body>\n"
		<< "<table class=\"three\">\n";
		

    while(i < o.size() - 2)
    {
    	OutFile
		<< "<tr>\n"
        << "<td class=\"four\"><p class=\"two\">" << o[i].Imie << "<br>" << o[i].Nazwisko <<"<br>" << o[i].Urodziny << "<br>" << o[i].Email << "<br>" << o[i].Wzrost << "<br>" << o[i].Numer1 << "<br>" << o[i].Numer2 << "<br>" << o[i].Numer3 << "<br>" << o[i].Plec << "</p></td>\n";
        i++;
        OutFile
        << "<td class=\"five\"><p class=\"one\">" << o[i].Imie << "<br>" << o[i].Nazwisko <<"<br>" << o[i].Urodziny << "<br>" << o[i].Email << "<br>" << o[i].Wzrost << "<br>" << o[i].Numer1 << "<br>" << o[i].Numer2 << "<br>" << o[i].Numer3 << "<br>" << o[i].Plec << "</p></td>\n"
		<< "</tr>\n";
        i++;
       
    }
    OutFile << "</table>\n" << "</body>\n" << "</html>\n";
    OutFile.close();
    return 0;
}
