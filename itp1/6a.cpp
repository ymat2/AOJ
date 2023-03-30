#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

int main() {
	int n;
	cin >> n;
	int vec[n];
	for (int i=0;i<n;i++) {
		cin >> vec[i];
	}
	for (int i=n;i>0;i--) {
		if (n-i) cout << " ";
		cout << vec[i-1];
	}
	/* which is more smart?
	for (int i=0;i<n;i++) {
		if (i) cout << " ";
		cout << vec[n-i-1];
	}
	*/
	cout << endl;
	return 0;
}
