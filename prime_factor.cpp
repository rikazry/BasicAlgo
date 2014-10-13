#include <iostream>
#include <vector>

using namespace std;

vector<int> prime_factors(int n){
    vector<int> factors;
    for (int i = 2; i <= n/i; ++i){
	int new_flag = 1;
	while (n % i == 0){
	    if(new_flag == 1){ factors.push_back(i); new_flag = 0;}
	    n /= i;
	}
    }
    if (n > 1)
	factors.push_back(n);
    return factors;
}

int main(){
    int n;
    cout << "enter an integer to find prime factors:\n";
    cin >> n;
    vector<int> factors = prime_factors(n);
    for(vector<int>::const_iterator i = factors.begin(); i != factors.end(); ++i){cout << *i << "\t";}
    cout << "\n";
    return 0;
}
