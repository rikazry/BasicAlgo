#include <iostream>
#include <vector>

using namespace std;

template <class T>
vector<T> unique_sorted(T a[], int n){
    vector<T> vec;//vector used to avoid resizing problem
    vec.reserve(n);//reserve room in advance to avoid reallocation
    vec.push_back(a[0]);
    for(int i = 1; i < n; ++i){
	if(a[i] != a[i-1]) vec.push_back(a[i]);
    }
    return vec;
}

int main(){
    int a[] = {1,1,3,3,3,5,5,5,9,9,9};
    int len = sizeof(a)/sizeof(a[0]);
    vector<int> vec = unique_sorted(a, len);
    for (vector<int>::const_iterator v = vec.begin(); v != vec.end(); ++v)
	cout << *v << ' ';
    return 0;
}
