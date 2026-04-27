#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    string name, name1;
    float rating, rating1;
    
    cin >> name >> rating;

    for (int i = 0; i <= n; i++) {
        cin >> name1 >> rating1;
        if (rating1 > rating) {
            name = name1;
            rating = rating1;
        } 
        
    }
    
    cout << name;
}
