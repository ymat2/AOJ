#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

int main() {
	int n;
	cin >> n;
	int arr[n];
	for (int i=0; i<n; i++) {
		cin>>arr[i];
	};
	for (int i=1; i<n; i++) {
		int v, j;
		v=arr[i];
		j = i-1;
		while (j >= 0 && arr[j] > v) {
			arr[j+1] = arr[j];
			j-- ;
		}
		arr[j+1] = v;
		for (int i=0; i<n-1; i++) {
			cout << arr[i] << " ";
		}
		cout << arr[n];
		cout << endl;
	}
	return 0;
}

