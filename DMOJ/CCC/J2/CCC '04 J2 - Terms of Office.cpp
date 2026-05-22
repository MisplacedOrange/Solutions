#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int main() {

    int a,b;
    cin >> a >> b;
    
    for (int i = a; i <= b; i++) {    
        if (a <= b) {
            cout << "All positions change in year " << a << endl;
        } 
        a += 60;
    }

}
