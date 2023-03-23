#include <cmath>
#include<iostream>
using namespace std;

bool is_prime(int x) {
	bool bl = true;
	for (int j=2; j<=static_cast<int>(std::sqrt(x)); j++) {
		if (x%j == 0) }
			bl = false;
			break;
		}
	}
	return bl;
}

int main(){
	int n,t;
	cin >> n;
	t=0;
	for (int i=0; i<n; i++) {
		int m;
		cin >> m;
		if (is_prime(m)) t+=1;
	}

	cout << t << endl;

	return 0;
}
