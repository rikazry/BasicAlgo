from __future__ import print_function


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None


class NodeDouble(Node):
    def __init__(self, data):
        super(NodeDouble, self).__init__(data)
        self.prv = None


class LinkedList(object):
    def __init__(self):
        self.head = None

    def append_node(self, data):
        new_node = Node(data)
        if self.head is not None:
            nxt = self.head.nxt
            while nxt is not None:
                nxt = nxt.nxt
            # below not working!!!
            nxt = new_node
        else:
            self.head = new_node

    def show(self):
        curr = self.head
        print(curr.data, end = '')
        while curr.nxt is not None:
            curr = curr.nxt
            print('->%d' %curr.data, end = '')

    def reverse_iter(self):
        prev = None
        curr = self.head
        while curr is not None:
            nxt = curr.nxt
            curr.nxt = prev
            prev = curr
            curr = nxt
        return prev

    def reverse_rec(self):
        pass


class DoublyLinkedList(LinkedList):
    def __init__(self):
        self.head = None

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
    dll = DoublyLinkedList()
    for i in xrange(10):
        dll.push(i)
    dll.show()
    print()
    dll.reverse()
    dll.show()




