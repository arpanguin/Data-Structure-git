class Node:
    __slots__ = "_element", "_next"

    def __init__(self, element, next=None):
        self._element = element
        self._next = next


class QueueUsingLinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def is_empty(self):
        """Checking if the queue is empty"""
        return self._size == 0

    def enqueue(self, element):
        """Insert element at the end of the queue"""
        node = Node(element)
        if self.is_empty():
            self._head = node
        else:
            self._tail._next = node
        self._tail = node
        self._size += 1

    def dequeue(self):
        """Removes the fist node i.e. Head node"""
        if not self.is_empty():
            p = self._head
            self._head = p._next
            self._size -= 1

    def display(self):
        if not self.is_empty():
            p = self._head
            while p:
                print(p._element, end="-->")
                p = p._next
        else:
            print("Queue is empty")


# queue = QueueUsingLinkedList()
# queue.dequeue()
# queue.display()
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.dequeue()
# queue.display()
