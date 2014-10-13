#include <iostream>

using namespace std;

long swap_bits(long x, const int &i, const int &j){
    if ( ((x >> i) & 1L) != ((x >> j) & 1L) )
        x ^= (1L << i) | (1L << j);
    return x;
}

int main(){
    long n = 12L;
    int i = 1, j = 2;
    cout << n << "\n";
    cout << swap_bits(n, i, j) << "\n";
    return 0;
}
