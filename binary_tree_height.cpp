#include <iostream>
#include <memory> //std::shared_ptr
#include <algorithm> //std::max

using namespace std;

template <typename T>
struct BinaryTree {
    T data;
    shared_ptr<BinaryTree <T> > left, right;
};

template <typename T>
int height(const shared_ptr<BinaryTree <T> > &tree, int count = -1){
    if (!tree) return count;
    return max(
        height(tree->left, count + 1),
	height(tree->right, count + 1));
}

int main(){
    BinaryTree<int> tree, tree1, tree2;
    tree.data = 0;
    tree1.data = 1;
    tree2.data = 2;
    tree.left = shared_ptr<BinaryTree <int> >(&tree1);
    tree1.right = shared_ptr<BinaryTree <int> >(&tree2);
    cout<<height(shared_ptr<BinaryTree <int> >(&tree))<<"\n";
    return 0;
}
