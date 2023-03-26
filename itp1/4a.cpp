#include<iostream>  // need for cout and endl
#include <cstdio>  // needed for printf
using namespace std;  // not recommended for general development

int main(){
	int a,b,d,r;
	double f;
	cin >> a >> b;

	d=a/b;
	r=a-b*d;
	f=(double)a/(double)b;

	printf("%d %d %.6lf\n",d,r,f);
	//cout << d << " " << r << " " << f << endl;

	return 0;
}
