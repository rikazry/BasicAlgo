#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool is_par_balanced(const string input){
    stack<char> par_stack;
    for(auto &c: input){
	if(c==')'){
	    if(par_stack.empty())
	        return false;
	    else if(par_stack.top()=='(')
		par_stack.pop();
	}
	else if(c=='(')
	    par_stack.push(c);
    }
    return par_stack.empty();
}

int main(){
    const string st1 = "(1+2)*3 + ((4+5)*6-7)*8";
    const string st2 = "(1+2)+3)";
    cout<<"string 1:\n";
    for(auto &c: st1)
	cout<<c;
    cout<<"\n"<<is_par_balanced(st1)<<"\n\n";
    cout<<"string 2:\n";
    for(auto &c:st2)
	cout<<c;
    cout<<"\n"<<is_par_balanced(st2)<<"\n\n";
    return 0;
}

