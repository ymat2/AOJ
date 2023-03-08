#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int a,b;
	cin >> a >> b;  // standard-in
	if ( a>b ) {
		cout << "a > b" << endl;
	} else if ( a==b ) {
		cout << "a == b" << endl;
	} else {
		cout << "a < b" << endl;
	}

	return 0;
}
