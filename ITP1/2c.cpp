#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int a,b,c;
	cin >> a >> b >> c;  // standard-in
	if ( a<b && b<c ) {
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}

	return 0;
}
