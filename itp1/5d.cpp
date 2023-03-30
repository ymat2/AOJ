#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

int main() {
	int n;
	cin >> n;

	for (int i=1; i<=n; i++) {
		if (i%3==0 || i%10==3) {
			cout << " " << i;
		} else {
			int t = i;
			while (t>0) {
				t /= 10;
				if (t%10==3) {
					cout << " " << i;
					break;
				}
			}
		}
	}
	cout << endl;
}
