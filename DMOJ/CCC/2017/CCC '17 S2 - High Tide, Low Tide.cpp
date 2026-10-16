#include <bits/stdc++.h>


using namespace std;

int main() {
    int n; cin >> n;
    vector<int> tide = {};


    for (int i = 0; i < n; i++) {
        int tidenum; cin >> tidenum;
        tide.push_back(tidenum);
    }

    sort(tide.begin(), tide.end());
    int mid = (n+1)/2;

    vector<int> hightide(tide.begin() + mid, tide.end());
    vector<int> lowtide(tide.begin(), tide.begin() + mid);
    reverse(lowtide.begin(), lowtide.end());

    int maxsize = max(lowtide.size(), hightide.size());

    for (int j = 0; j < maxsize; ++j) {
        if (j < lowtide.size()) {
            cout << lowtide[j] << " ";
        }

        if (j < hightide.size()) {
            cout << hightide[j] << " ";
        }
    }

    return 0;
    
}