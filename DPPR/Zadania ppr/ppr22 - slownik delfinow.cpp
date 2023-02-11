#include<iostream>
#include<list>
#include<string>
using namespace std;
list<string> lst;
list<string>::iterator ite;

int main()
{
	int n;
	cin >> n;
	for(int i=0;i<n;i++)
	{
		string tmp;
		cin>>tmp;
		lst.push_front(tmp);
	}

	lst.sort();
	for(ite=lst.begin();ite!=lst.end();ite++) cout<<(*ite)<<endl;
	cout<<endl;
	
	
return 0;
}
