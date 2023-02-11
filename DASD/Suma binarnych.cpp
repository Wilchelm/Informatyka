#include <iostream>
using namespace std;

int main()
{
    int d,n,n_tab[10000],m,m_tab[10000],result[10000],c;
    cin >> d;
    for (int ii=0; ii<d; ii++)
    {
        for (int i=0; i<10000;i++)
        {
            m_tab[i]=0;
            n_tab[i]=0;
        }
        cin >> n;
        for (int i=n-1; i>=0; i--)
            cin >> n_tab[i];
        cin >> m;
        for (int i=m-1; i>=0; i--)
            cin >> m_tab[i];
        c=0;
        if(n>m)
		{
			for(int i=0;i<n+1;i++)
			{
				result[i] = (n_tab[i] + m_tab[i] + c) %2;
				c = (n_tab[i] + m_tab[i] + c) / 2;
			}
        	result[n] = c;
            if (c == 1)
			{
	            for(int i=n;i>=0;i--)
				{
	            	cout << result[i];
	            }
            }
            else 
			{
            	for(int i=n-1;i>=0;i--)
				{
                	cout << result[i];
                }
            }
		}
		else if(m>=n)
		{
			for(int i=0;i<m;i++)
			{
				result[i] = (n_tab[i] + m_tab[i] + c) %2;
				c = (n_tab[i] + m_tab[i] + c) / 2;
			}
        	result[m] = c;
            if (c == 1)
			{
	            for(int i=m;i>=0;i--)
				{
	            	cout << result[i];
	            }
            }
            else 
			{
            	for(int i=m-1;i>=0;i--)
				{
                	cout << result[i];
                }
            }
		}
	}
return 0;
}
