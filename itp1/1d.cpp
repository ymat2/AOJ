#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int S,h,m,s;
	cin >> S;  //standard-in
	s=S%3600%60;
	m=(S-s)%3600/60;
	h=S/3600;
	cout << h << ":" << m << ":" << s << endl;  //standard-out
	return 0;
}
