#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

int main() {
	int n;
	cin >> n;
	int v[4][13];
	for (int i=0; i<n; i++) {
		char s;
		int j;
		cin >> s >> j;
		if (s=='S') {
			v[0][j-1] = 1;
		} else if (s=='H') {
			v[1][j-1] = 1;
		} else if (s=='C') {
			v[2][j-1] = 1;
		} else if (s=='D') {
			v[3][j-1] = 1;
		}
 	}

 	char idx[] = {'S', 'H', 'C', 'D'};

 	for (int i=0; i<4; i++) {
		for (int j=0; j<13; j++) {
			if (v[i][j] != 1) {
				cout << idx[i] << " " << j+1 << endl;
			}
		}
	}

	return 0;
}
