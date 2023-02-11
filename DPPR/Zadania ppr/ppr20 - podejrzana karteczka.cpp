#include <iostream>
#include <string>
 
using namespace std;
 
int main()
{
    int n = 0;
    cin >>n;
    cin.ignore();
    int* litery = new int[n];
    int* cyfry = new int[n];
    string* linia = new string[n];
    for (int i=0; i<n; i++)
        {
        getline(cin,linia[i]);
        }
   for(int i=0 ; i<n ; i++)
    {
        cyfry[i]=0;
        litery[i]=0;
    for(unsigned int j=0; j<linia[i].length(); j++)
                {
            if (isdigit(linia[i][j]))
                {
                        cyfry[i]++;
                }
            else if((linia[i][j]>='a' && linia[i][j]<='z') || (linia[i][j]>='A' && linia[i][j]<='Z'))
                {
                        litery[i]++;
                }
                }
    cout << linia[i].length() << " " << litery[i] << " " << cyfry[i] << endl;
                }
 return 0;
}
