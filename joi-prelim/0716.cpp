#include<iostream>
using namespace std;

int main(){
	int S,A,B,m,i;
	cin >> S >> A >> B;
	m=250;
	i=0;

	while (S>A+B*i) {
		i++;
		m+=100;
	}

	cout << m << endl;

	return 0;
}
