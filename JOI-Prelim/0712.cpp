#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int a,b;
	cin >> a >> b;
	if ((a+b)%12==0) {
		cout << 12 << endl;
	} else {
		cout << (a+b)%12 << endl;
	}
	return 0;
}
