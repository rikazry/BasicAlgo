#include <iostream>

using namespace std;

//factorial for 
int factorial_for(int n){
    int output = 1;
    for (int i = 2; i <= n; ++i)
	output *= i;
    return output;
}

//factorial recursive
int factorial_rec(int n){
    if (n == 0) return 1;
    return n * factorial_rec(n-1);
}

//factorial tail recursive
int factorial_tail(int n, int last = 1){
    if (n == 0) return last;
    return factorial_tail(n-1, n * last);
}

int main(){
    int n;
    cout << "enter an integer for factorial calculation:\n";
    cin >> n;
    cout << "iteration result:" << "\t" << factorial_for(n) << "\n";
    cout << "recursion result:" << "\t" << factorial_rec(n) << "\n";
    cout << "tail recursion result:" << "\t" << factorial_tail(n) << "\n";
    return 0;
}
