import java.util.Scanner;

public class temp {

    public static int consecStones(String s) {

        if (s.length() <= 1) {
            return 0;
        }

        if (s.charAt(0) == s.charAt(1)) {
            return 1 + consecStones(s.substring(1));
        }

        return consecStones(s.substring(1));
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int n = sc.nextInt();
        String s = sc.next();

        System.out.println(consecStones(s));

    }
}

/*
C++ Solution

#include <bits/stdc++.h>


using namespace std;


int consecStones(std::string s) {
    if (s.length() <= 1) {
        return 0;
    }

    if (s[0] == s[1]) {
        return 1 + consecStones(s.substr(1));
    }

    return consecStones(s.substr(1));
    
}

int main() {
    int n;
    std::string s;
    cin >> n >> s;
    cout << consecStones(s);
}

*/