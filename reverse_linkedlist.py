from __future__ import print_function


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None

    def link_node(self, data):
        if self.nxt is None:
            self.nxt = Node(data)
        else:
            self.nxt.link_node(data)


class NodeDouble(Node):
    def __init__(self, data):
        super(NodeDouble, self).__init__(data)
        self.prv = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append_node(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            self.head.link_node(data)

    def show(self):
        curr = self.head
        print(curr.data, end='')
        while curr.nxt is not None:
            curr = curr.nxt
            print('->%d' % curr.data, end='')

    def reverse_iter(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.nxt
            curr.nxt = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_rec(self):
        pass


class DoublyLinkedList(LinkedList):

    def push(self, data):
        """
        insert at head
        :param data:
        :return:
        """
        new_node = NodeDouble(data)
        new_node.nxt = self.head
        if self.head is not None:
            self.head.prv = new_node
        self.head = new_node

    def reverse(self):
        temp = None
        current = self.head

        # iterate from head to tail
        while current is not None:
            # swap prv and nxt
            temp = current.prv
            current.prv = current.nxt
            current.nxt = temp
            # move on to original nxt
            current = current.prv

        # edge case: empty list / one-node list
        if temp is not None:
            # point head to last node (last node's original's prv's original nxt)
            self.head = temp.prv


if __name__ == "__main__":

    print("### Single Linked List ###")
    ll = LinkedList()
    for i in xrange(10):
        ll.append_node(i)
    ll.show()
    print()
    ll.reverse_iter()
    ll.show()
    print()

    print("### Double Linked List ###")
    dll = DoublyLinkedList()
    for i in xrange(10):
        dll.push(i)
    dll.show()
    print()
    dll.reverse()
    dll.show()
    print()




