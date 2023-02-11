#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int main()
{
    vector <int>  powtarzanie;
    int n, x;
    cin >> n;
    for (int i = 0; i<n; i++)
    {
        cin >> x;
        powtarzanie.push_back(x);
    }
    sort(powtarzanie.begin(),powtarzanie.end());
    int p=0;
    for (int k = 1; k<n; k++) {
            if (powtarzanie[k] == powtarzanie[k-1] && powtarzanie[k] != p)
            {
                cout << powtarzanie[k];
                p = powtarzanie[k];
            }
    }
    return 0;
}
