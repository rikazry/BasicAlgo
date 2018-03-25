from __future__ import print_function

class Node(object):
    def __init__(self, data, nxt = None):
        self.data = data
        self.nxt = nxt

class LinkedList(object):
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if(self.head is not None):
            nxt = self.head.nxt
            while(nxt is not None):
                nxt = nxt.nxt
            nxt = new_node
        else:
            self.head = new_node

    def show(self):
        curr = self.head
        print(curr.data, end = '')
        while(curr.nxt is not None):
            print('->%d' %curr.nxt.data, end = '')

    def reverse_iter(self):
        prev = None
        curr = self.head
        while(curr is not None):
            nxt = curr.nxt
            curr.nxt = prev
            prev = curr
            curr = nxt
        return prev

    def reverse_rec(self):
        pass





