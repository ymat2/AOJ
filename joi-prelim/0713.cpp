#include<iostream>
using namespace std;

int main(){
	int N;
	string S;
	cin >> N >> S;
	for (int i=0; i=N-1; i++) {
		if (S[i] == "J") {
			cout << S[i-1] << endl;
		}
	}

	return 0;
}
