#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int n, x, y, z;
    cin >> n;
    int totalx = 0, totaly= 0, totalz = 0;

    for (int i = 0; i < n ; i++) {
        cin >> x >> y >> z;
        totalx += x;
        totaly += y;
        totalz += z;
    }

    if (totalx == 0 && totaly == 0 && totalz == 0){
        cout << "YES" << endl;
    } else {
        cout << "NO" << endl;
    }

    return 0;
}
