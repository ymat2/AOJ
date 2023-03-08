#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int i,x;
	i = 0;
	while (1) {
		cin >> x;
		if ( x==0 ) {
			break;
		} else {
			i += 1;
			cout << "Case " << i << ": " << x << endl;
		}
	}

	return 0;
}
