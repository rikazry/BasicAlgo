#include <iostream>

using namespace std;

//factorial for 
int factorial_for(int n){
    int output = 1;
    for (int i = 2; i <= n; ++i)
	output *= i;
    return output;
}
//fib for
int fib_for(int n){
    if (n == 0 || n == 1) return n;
    int prev = 0, last = 1, temp;
    for (int i = 2; i <= n; ++i){
	temp = last;
        last = prev + last;
	prev = temp;
    }
    return last;
}

//factorial recursive
int factorial_rec(int n){
    if (n == 0) return 1;
    return n * factorial_rec(n-1);
}
//fib recursive
int fib_rec(int n){
    if (n == 0 || n == 1) return n;
    else return fib_rec(n-1) + fib_rec(n-2);
}

//factorial tail recursive
int factorial_tail(int n, int last = 1){
    if (n == 0) return last;
    return factorial_tail(n-1, n * last);
}
//fib tail recursive
int fib_tail(int n, int last = 1, int prev = 0){
    if (n == 0) return prev;
    if (n == 1) return last;
    return fib_tail(n-1, last+prev, last);
}

int main(){
    int n;
    cout << "enter an integer for factorial/fibonacci calculation:\n";
    cin >> n;
    cout << "n! iteration result:" << "\t" << factorial_for(n) << "\n";
    cout << "n! recursion result:" << "\t" << factorial_rec(n) << "\n";
    cout << "n! tail recursion result:" << "\t" << factorial_tail(n) << "\n";
    cout << "fib(n) iteration result:" << "\t" << fib_for(n) << "\n";
    cout << "fin(n) recursion result:" << "\t" << fib_rec(n) << "\n";
    cout << "fib(n) tail recursion result:" << "\t" << fib_tail(n) << "\n";
    return 0;
}
