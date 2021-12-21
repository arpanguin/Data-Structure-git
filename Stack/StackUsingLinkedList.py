"""we consider head for push and pop since head takes O(1) and O(1) and Tail takes O(1) and O(n) for pop """


class Node:
    """Class for linked list node"""
    __slots__ = ["_element", "_next"]

    def __init__(self, element, next):
        self._element = element
        self._next = next


class StackUsingLinkedList:
    """Class to create stack using linked list"""
    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        """Checking the element length"""
        return self._size

    def is_empty(self):
        """Checking if stack is empty"""
        return self._size == 0

    def push(self, element):
        """Pushing the element in front i.e. in head"""
        node = Node(element, None)
        if self.is_empty():
            self._head = node
        else:
            node._next = self._head
            self._head = node
        self._size += 1

    def pop(self):
        """Popping the element from beginning of linked list i.e. from tail"""
        if not self.is_empty():
            self._head = self._head._next
            self._size -= 1

    def display(self):
        """Displaying the element"""
        print()
        p = self._head
        while p:
            print(p._element, end="-->")
            p = p._next


# s_linked_list = StackUsingLinkedList()
# s_linked_list.push(2)
# s_linked_list.push(3)
# s_linked_list.push(4)
# s_linked_list.push(5)
# s_linked_list.display()
# s_linked_list.pop()
# s_linked_list.display()
# s_linked_list.pop()
# s_linked_list.display()
# s_linked_list.pop()
# s_linked_list.display()
# s_linked_list.pop()
# s_linked_list.display()

