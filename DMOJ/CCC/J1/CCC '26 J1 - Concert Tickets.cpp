#include <iostream>

using namespace std;

int main() {
    int b, t, p;
    cin >> b >> t >> p;

    int x = t-p;

    if (b <= x) {
        cout << 'Y' << ' ' << (x-b) << endl;
    } else {
        cout << 'N' << endl;
    }

    return 0;
}
