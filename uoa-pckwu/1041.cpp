#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int n,s;

	while(1) {
		cin >> n;
		if ( n==0 ) {
			break;
		} else {
			int s;
			s=0;
			for (int i=0; i<n/4; i++) {
				int t;
				cin >> t;
				s+=t;
			}
			cout << s << endl;
		}
	}
	return 0;
}
