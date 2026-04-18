#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int x;
    vector<int> nums;

    for (int i = 0; i < 5; i++) {
        cin >> x;
        nums.push_back(x);
    }
    int D;
    cin >> D;

    sort(nums.begin(), nums.end());

    int t = 0;
    for (size_t i = 1; i < nums.size() - 1; i++) {
        t += nums[i];
    }

    cout << (t * D) << endl;
    return 0;
}
