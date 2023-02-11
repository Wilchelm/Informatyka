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
    OutFile.open("Nif.html", ios_base::out);

    unsigned int i = 0;
    OutFile << "<!doctype html>\n" <<
    "<html>\n" <<
	"<head>\n" <<
	"<title>Nif.html</title>\n" <<
	"<meta charset=UTF-8\" /> \n" <<
	"</head>\n" <<
	"<center>\n	<table width=\"667\" border=\"1\" bordercolor=\"#000000\" cellpadding=\"2\" cellspacing=\"0\">\n		<colgroup><col width=\"328\">\n		<col width=\"328\">\n		</colgroup><tbody><tr valign=\"TOP\">\n";

    while(i < o.size() - 2)
    {
    	OutFile << "			<td width=\"328\">\n";
        OutFile << "				<p align=\"CENTER\" style=\"margin-bottom: 0in; color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Imie << " " << o[i].Nazwisko <<"</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Urodziny << "</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Email << "</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Wzrost << "</p>\n"  << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Numer1 << "</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Numer2 << "</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Numer3 << "</p>\n" << "				<p style=\"color: #fa00ff; face: Calibri, sans-serif\">" << o[i].Plec << "</p>\n";
        OutFile << "			</td>\n";
        i++;
        OutFile << "			<td width=\"328\">\n";
        OutFile << "				<p align=\"RIGHT\" style=\"margin-bottom: 0in; color: #fa00ff; face: Tahoma, sans-serif; font-size=4; font-size: 15pt; background: #0d0150\">" << o[i].Imie << " " << o[i].Nazwisko <<"</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Tahoma, sans-serif; size: 4; font-size: 15pt; background: #0d0150\">" << o[i].Urodziny << "</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Tahoma, sans-serif; size: 4; font-size: 15pt; background: #0d0150\">" << o[i].Email << "</p>\n" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Tahoma, sans-serif; size: 4; font-size: 15pt; background: #0d0150\">" << o[i].Wzrost << "</p>\n"  << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Tahoma, sans-serif; size: 4; font-size: 15pt; background: #0d0150\">" << o[i].Numer1 << "</p>" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Tahoma, sans-serif; size: 4; font-size: 15pt; background: #0d0150\">" << o[i].Numer2 << "</p>" << "				<p style=\"margin-bottom: 0in; color: #fa00ff; face: Tahoma, sans-serif; size: 4; font-size: 15pt; background: #0d0150\">" << o[i].Numer3 << "</p>" << "				<p 	style=\"color: #fa00ff; face: Tahoma, sans-serif; size: 4; font-size: 15pt; background: #0d0150\">" << o[i].Plec << "</p>\n";
        OutFile << "			</td>\n";
        OutFile << "		</tr>\n";
		i++;
    }
    OutFile << "	</tbody></table>\n" << "</center>\n" << "<p style=\"margin-bottom: 0in\"><br>\n" << "</p>\n\n" << "</body></html>";
    return 0;
}
