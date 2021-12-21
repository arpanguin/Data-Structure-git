class QueueUsingArray:
    def __init__(self, data=[]):
        self._data = data

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return self.__len__() == 0

    def enqueue(self, element):
        """Insert element at the end of list"""
        self._data.append(element)

    def dequeue(self):
        """Removing the fist element is queue"""
        if not self.is_empty():
            return self._data.pop(0)

    def top(self):
        """Returns the first element"""
        if not self.is_empty():
            return self._data[0]

    def display(self):
        """Display the queue"""
        if not self.is_empty():
            print('-->'.join(str(i) for i in self._data))
        else:
            print("Queue is empty")


# queue = QueueUsingArray()
#
# print("Initial queue....")
# queue.enqueue(2)
# queue.enqueue(3)
# queue.enqueue(4)
# queue.display()
#
# print("\nAdding 6 queue....")
# queue.enqueue(6)
# queue.display()
#
# print(f"\nAfter the dQueue operation done. i.e. removed : {queue.dequeue()}")
# queue.display()
#
# print(f"\nLets get the top element : {queue.top()}")
#
# print("\nAfter dQueueing all the elements.....")
# queue.dequeue()
# queue.dequeue()
# queue.dequeue()
# queue.display()

