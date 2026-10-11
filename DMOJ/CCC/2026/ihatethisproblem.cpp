#include <bits/stdc++.h>
using namespace std;

int main() {
    long long A, B, K;
    int T;

    cin >> A >> B >> K >> T;

    long long distance = abs(B - A);
    long long gHops = distance / K;
    long long remainder = distance % K;

    long long normal = gHops + remainder;
    long long ovr = gHops + 1 + K - remainder;

    long long minimum = min(normal, ovr);

    if (T == 1) {
        cout << minimum;
    } else {
        long long second = minimum + 2;

        if (abs(normal - ovr) == 1 ||(K == 2 && distance > 0)) {
            second = minimum + 1;
        }

        cout << second;
    }

    return 0;
}
// Straight aired durring ccc'26