#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int x,y,z;
	cin >> x >> y >> z;
	if (x+y>z) {
		cout << 0 << endl;
	} else {
		cout << 1 << endl;
	}

	return 0;
}
