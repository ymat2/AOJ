#include <bits/stdc++.h>  //import all the c++ libraries
using namespace std;

int main(){

	while (true) {
		int H,W;
		cin >> H >> W;

		if (H==0 && W==0) {
			break;
		} else {
			for (int i=0;i<H;i++) {
				for (int j=0;j<W;j++) {
					cout << "#";
				}
				cout << endl;
			}
			cout << endl;
		}
	}
}
