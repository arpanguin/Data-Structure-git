class Node:
    __slots__ = '_element', '_prev', '_next'  # instance variables

    def __init__(self, element, prev, next):
        self._element = element
        self._prev = prev
        self._next = next


class DoublyLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self.size = 0

    def is_empty(self):
        """Checking if doubly linked list is empty"""
        return self.size == 0

    def add_node(self, element):
        """Adding new node at the end of doubly linked list"""
        new_item = Node(element, None, None)
        if self.is_empty():
            self._head = new_item
        else:
            new_item._prev = self._tail
            self._tail._next = new_item
        self._tail = new_item
        self.size += 1

    def display(self):
        """Displaying the doubly linked list"""
        p = self._head
        while p:
            print(p._element, end="-->")
            p = p._next


d_list = DoublyLinkedList()

print("Initial doubly linked list : ")
d_list.add_node(23)
d_list.add_node(24)
d_list.add_node(25)
d_list.display()
