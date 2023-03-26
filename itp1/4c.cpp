#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	for (;;) {
		int a,b;
		char op;
		cin >> a >> op >> b;

		if (op=='?') {
			break;
		} else if (op=='+') {
			cout << a+b << endl;
		} else if (op=='-') {
			cout << a-b << endl;
		} else if (op=='*') {
            cout << a*b << endl;
        } else if (op=='/') {
            cout << a/b << endl;
        }
	}

	return 0;
}
