#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

bool is_prime(int i) {
	bool bl = true;
	for (int j=2;j<=sqrt(i);j++) {
		if (i%j == 0){
			bl = false;
			break;
		}
	}
	return bl;
}

int main() {
	int n;
	cin >> n;
	cout << n << ":";

	while (is_prime(n)==false) {
		for (int i=2;i<=sqrt(n);i++) {
			if (n%i == 0) {
				cout << " " << i;
				n /= i;
				break;
			}
		}
	}
	cout << " " << n << endl;
	return 0;
}

