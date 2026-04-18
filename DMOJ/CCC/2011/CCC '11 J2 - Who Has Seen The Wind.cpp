#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>

using namespace std;

int main() {
    int h, m;
    int a = 0;
    int i = 1;
    cin >> h >> m;

    while (true) {
        
        a = -6*(std::pow(i, 4)) + h*(std::pow(i, 3)) + 2*(std::pow(i, 2)) + i;
        if (a <= 0) {
            cout << "The balloon first touches ground at hour:" << endl << i;
            return 0;
        } 
        if (i == m){
            cout << "The balloon does not touch ground in the given time." << endl;
            return 0;
        }
        i++;
    }
    
    
    
    

}