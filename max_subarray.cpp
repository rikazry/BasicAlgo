#include <iostream>
#include <vector>
#include <algorithm> //std::max

using namespace std;

template <typename T>
T max_sub_array(vector<T> const & numbers){
    T max_ending = 0, max_so_far = 0;
    for(auto & number: numbers){
	max_ending = max(0, max_ending + number);
	max_so_far = max(max_so_far, max_ending);
    }
    return max_so_far;
}

double maxSubarray(double A[], int len, int &i, int &j){
    double T = A[0], Vmax = A[0];
    double Tmin = min(0.0, T);
    for(int k = 1; k < len; ++k){
	T += A[k];
	if (T - Tmin > Vmax) {Vmax = T - Tmin; j = k;}
	if (T < Tmin) {Tmin = T; i = k+1;}//problem checking index i < j
    }
    return Vmax;
}

int main(){
    double A[] = {1.,2.,-5.,4.,-3.,2.,6.,-5.,-1.};
    int i = 0, j = 0;
    int len = sizeof(A)/sizeof(A[0]);
    for(int k = 0; k < len; ++k){cout << A[k] << "\t";}
    cout << "\n" << maxSubarray(A, len, i, j) << "\n";
    cout << i << "\t" << j << "\n";
    for(int k = i; k <= j; ++k){cout << A[k] << "\t";}
    return 0;
}
