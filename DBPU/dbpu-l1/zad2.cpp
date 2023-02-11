#include <iostream> 
#include <cstring> 
#include <fstream>
#include <string>
using namespace std; 
int main() 
{ 
    string path, word;

    cout << "Enter file path: "; 
    getline(cin, path); 

    cout << "Enter word to search in file: ";
    getline(cin, word);

    ifstream file(path);
    if(file.fail()){
        cout << "File not exist.\n";
    }
    if (file.is_open()) {
        string line;
        while (getline(file, line)) {
            size_t found = line.find(word); 
            if (found != string::npos) 
                cout << line << endl; 
        }
    file.close();
    }

    return 0; 
} 
