#include<iostream>  // need for cout and endl
#include <cstdio>  // needed for printf
using namespace std;  // not recommended for general development

int main(){
	double r,S,L;
	double pi = 3.141592653589;
	cin >> r;

	S=r*r*pi;
	L=2*pi*r;

	printf("%.6lf %.6lf\n",S,L);
	//cout << d << " " << r << " " << f << endl;

	return 0;
}
