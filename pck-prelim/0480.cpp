#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

int main() {

	int d1, m1, d2, m2;
	bool a;
	cin >> d1 >> m1;
	cin >> d2 >> m2;

	if ((d1 > 37) || (d1 == 37 && m1 >= 5)) {
		cout << 2 << endl;
	} else if ((d1 > d2)  || (d1 == d2 && m1 >= m2)) {
		cout << 1 << endl;
	} else {
		cout << 0 << endl;
	}

	return 0;
}

