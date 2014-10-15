#include <memory> // shared_ptr
#include <iostream>

using namespace std;

template<typename T>
struct node_t {
    T data;
    shared_ptr<node_t<T> > next;
};

//recursive
template<typename T> 
shared_ptr<node_t<T> > reverse_linked_list(const shared_ptr<node_t<T> > &head){
    if (!head || !head->next){
	return head;
    }
    shared_ptr<node_t<T> > new_head = reverse_linked_list(head->next);
    head->next->next = head;
    head->next = nullptr;
    return new_head;
}

//while
template<typename T>
shared_ptr<node_t<T> > reverse_linked_list_iter(const shared_ptr<node_t<T> > &head){
    shared_ptr<node_t<T> > prev = nullptr, curr = head;
    while(curr){
	shared_ptr<node_t<T> > next = curr->next;
	curr->next = prev;
	prev = curr;
	curr = next;
    }
    return prev;
}

int main(){
    node_t<int> n1;
    n1.data = 1;
    node_t<int> n2;
    n2.data = 2;
    n1.next = shared_ptr<node_t<int> >(&n2);
    cout <<n1.data<<"->"<<n1.next->data;
    shared_ptr<node_t<int> > n0 = shared_ptr<node_t<int> >(&n1);
    shared_ptr<node_t<int> > N1 = reverse_linked_list(n0);
    cout <<N1->data<<"->"<<N1->next->data;
    return 0;
}
