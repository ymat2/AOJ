#include <iostream>
#include <vector>
#include <algorithm>
#include <numeric>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> l(n);
    for (int i = 0; i < n; i++) {
        cin >> l[i];
    }
    int min_val = *min_element(l.begin(), l.end());
    int max_val = *max_element(l.begin(), l.end());
    long long sum_val = accumulate(l.begin(), l.end(), 0);
    cout << min_val << " " << max_val << " " << sum_val << endl;
    return 0;
}
