#include <bits/stdc++.h>
using namespace std;
 
int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(nullptr),cout.tie(nullptr);
    int t;
    cin>>t;
    while(t--){
        long long a, b, x, y, n, tmp; 
        cin >> a >> b >> x >> y >> n;
        if(max(a-n, x) < max(b-n, y)) {
            tmp = max(a-n, x);
            tmp = n - (a - tmp);
            cout << max(a-n, x) * max(b-tmp, y) << '\n';
        } else {
            tmp = max(b-n, y);
            tmp = n - (b - tmp);
            cout << max(a-tmp, x) * max(b-n, y) << '\n'; 
        }
    }
}