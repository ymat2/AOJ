#include<iostream>
using namespace std;

int main(){
	int s,t;
	cin >> s >> t;
	if (s+t >= s-t) {
		cout << s+t << endl;
		cout << s-t << endl;
	} else {
		cout << s-t << endl;
		cout << s+t << endl;
	}

	return 0;
}
