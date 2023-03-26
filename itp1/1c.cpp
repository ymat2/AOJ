#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int a,b,S,L;
	cin >> a >> b;  //standard-in
	S=a*b;
	L=2*(a+b);
	cout << S << " " << L << endl;  //standard-out
	return 0;
}
