#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int main() {

    int n, t;
    cin >> n;

    for (int i = 0; i < n; i++) {
        cin >> t;
        if (t % 3 != 0) {
            cout << "First" << endl;
        } else {
            cout << "Second" << endl;
        }
    }

}
