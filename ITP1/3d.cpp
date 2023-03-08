#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int a,b,c,x;
	cin >> a >> b >> c;

	x = 0;
	for (int i=a; i<=b; i++) {
		if (c%i==0) {
			x++;
		} else {
			x+=0;
		}
	}

	cout << x << endl;

	return 0;
}
