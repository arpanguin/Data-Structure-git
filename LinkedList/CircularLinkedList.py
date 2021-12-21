class Node:
    __slots__ = '_element', '_next'  # instance variables

    def __init__(self, element, next):
        self._element = element
        self._next = next


class CircularLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        """Checking if linked list is empty"""
        return self._size == 0

    def add_node(self, element):
        """Adding node in the last position in circular linked list"""
        new_item = Node(element, None)
        if self.is_empty():
            self._head = new_item  # Because this is first node
        else:
            self._tail._next = new_item  # Because we need to add the new node in the last item of current node
            new_item._next = self._head

        self._tail = new_item
        self._size += 1

    def add_beginning(self, element):
        """Adding a new node at the beginning of linked list"""
        if self.is_empty():
            self.add_node(element)
        else:
            new_item = Node(element, self._head)
            self._head = new_item
            self._tail._next = new_item
            self._size += 1

    def display(self):
        """Displaying a circular linked list"""
        p = self._head
        i=1
        if self._head is None:
            print("List is Empty")
        else:
            while i <= self._size:
                print(p._element, end="-->")
                p = p._next
                i += 1


c_list = CircularLinkedList()

print("After adding items in list : ")
c_list.add_node(23)
c_list.add_node(24)
c_list.add_node(25)
c_list.display()

print("\n\nAfter adding 22 at the beginning :")
c_list.add_beginning(22)
c_list.display()



