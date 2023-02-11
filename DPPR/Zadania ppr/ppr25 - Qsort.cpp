#include<iostream>
#include<algorithm>
using namespace std;

int main()
{
	int D;
	cin >> D;
	for(int d=0;d<D;d++)
	{
	int N;
	cin >> N;
	int tab[N];
	for(int i=0; i<N; i++) 
	{
		cin >> tab[i];
	}
	
	sort(tab, tab + N, greater < int >() );
	
	for( int j = 0; j < N; j++ )
         cout << tab[ j ] << " ";
     }
	
	return 0;
}
