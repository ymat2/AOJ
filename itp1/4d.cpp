#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

int main() {
	int n, tmin, tmax;
	long long tsum = 0;
	cin >> n;
	tmin = INT_MAX;
	tmax = INT_MIN;
	for (int i=0;i<n;i++) {
		int t;
		cin >> t;
		tsum += t;

		tmax = max(t, tmax);
		tmin = min(t, tmin);

	}
	cout << tmin << " " << tmax << " " << tsum << endl;
}
