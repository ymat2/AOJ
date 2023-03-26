#include<iostream>  // need for cout and endl
using namespace std;  // not recommended for general development

int main(){
	int W,H,x,y,r;
	cin >> W >> H >> x >> y >> r;  // standard-in
	if ( r<=x && x<=W-r && r<=y && y<=H-r ) {
		cout << "Yes" << endl;
	} else {
		cout << "No" << endl;
	}

	return 0;
}
