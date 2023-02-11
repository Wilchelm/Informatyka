#include <iostream>
#include <iomanip>
using namespace std;

int main() {
	unsigned int u, n, s;
	cin >> u >> n >>s;
double x=s/(((double) u)/2+n);
	cout << fixed << setprecision(2) << x;
	return 0;
}


