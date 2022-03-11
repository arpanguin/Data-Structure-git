class Node:
    __slots__ = '_element', '_next'  # instance variables

    def __init__(self, element, next):
        self._element = element
        self._next = next


class LinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        """Checking if the linked list is empty"""
        return self._size == 0

    def add_tail(self, element):
        """Adding the new element at the tail of linked list"""
        new_item = Node(element, None)
        if self.is_empty():
            self._head = new_item  # Because this is first node
        else:
            self._tail._next = new_item  # Because we need to add the new node in the last item of current node
        self._tail = new_item
        self._size += 1

    def add_head(self, element):
        """Adding a new element at the beginning of linked list"""
        if self.is_empty():
            self.add_tail(element)
        else:
            node = Node(element, self._head)
            self._head = node
        self._size += 1

    def add_position(self, element, position):
        node = Node(element, None)
        if position <= self._size + 1:
            p = self._head
            i = 0
            if position == 1:
                self.add_head(element)
            elif position == self._size + 1:
                self.add_tail(element)
            else:
                while i <= position - 2:
                    if i == position - 2:
                        temp = p._next
                        p._next = node
                        node._next = temp
                    i += 1
                    p = p._next
            self._size += 1

    def insert_sorted(self, element):
        """Insert the element in sorted order"""
        node = Node(element, None)
        if self.is_empty():
            self._head = node
        else:
            p = self._head
            q = self._head
            while p and p._element < element:
                q = p
                p = p._next
            if p == self._head:
                node._next = p
                self._head = node
            else:
                node._next = q._next
                q._next = node
        self._size += 1

    def delete_beginning(self):
        if not self.is_empty():
            p = self._head
            self._head = p._next
            self._size -= 1

    def delete_end(self):
        if not self.is_empty():
            p = self._head
            for i in range(self._size):
                if i == self._size - 2:
                    p._next = None
                    self._size -= 1
                    break
                p = p._next

    def delete_position(self, position):
        p = self._head
        i = 1
        while i <= position - 1:
            if i == position - 1:
                p._next = p._next._next
                self._size -= 1
                break
            p = p._next

    def display(self):
        p = self._head
        while p:
            print(p._element, end='-->')
            p = p._next

    def search(self, search_key):
        p = self._head
        index = 0
        while p:
            if p._element == search_key:
                return index
            p = p._next
            index += 1
        return -1

    def removeDuplicatesFromLinkedList(self):
        linkedList = self._head
        while linkedList:
            p = linkedList._next
            if p and linkedList._element == linkedList._element.value:
                p = p._next
                linkedList._next = p
            linkedList = linkedList._next
        return linkedList

    def findMid(self):
        """Return the middle element of the linkedlist"""
        head = self._head
        fast = head
        slow = head
        moveBool = True
        while fast._next != None:
            fast = fast._next
            if moveBool:
                slow = slow._next
            moveBool = not moveBool
        return slow._element

    def sumOfLinkedLists(self, list_l1, list_l2):
        """Add two linked list and return a new list"""
        linkedListOne = list_l1._head
        linkedListTwo = list_l2._head

        remaining_val = 0

        while linkedListOne or linkedListTwo:
            if linkedListOne and linkedListTwo:
                addition = linkedListOne._element + linkedListTwo._element + remaining_val
            elif linkedListOne:
                addition = linkedListOne._element + remaining_val
            else:
                addition = linkedListTwo._element + remaining_val

            remaining_val = int(str(addition)[0] if len(str(addition)) > 1 else 0)
            addition = int(str(addition)[1] if len(str(addition)) > 1 else str(addition)[0])

            self.add_tail(addition)
            linkedListOne = linkedListOne._next if (linkedListOne and linkedListOne._next) else None
            linkedListTwo = linkedListTwo._next if (linkedListTwo and linkedListTwo._next) else None
        self.display()

    def reverse(self, l1):
        head = l1._head
        if not head._next:
            return head
        p = head
        q = None
        while p:
            temp = p._next
            p._next = q
            q = p
            p = temp
        return q

node = LinkedList()

print("Initial Linked List :")
node.add_tail(1)
node.add_tail(2)
node.add_tail(3)
node.add_tail(4)
node.add_tail(5)
# node.add_tail(4)
# node.add_tail(5)
# node.add_tail(6)
# node.add_tail(6)
node.display()
node1 = LinkedList()
node1.reverse(node)
node1.display()
# print("\n\nAfter adding 22 in the beginning :")
# node.add_head(22)
# node.display()
#
# print(f"\n\nMiddle element is ==> {node.findMid()}")
#
# print(f"\n23 is at position : {node.search(23)}")
#
# print("\nAfter adding 26 in specified position :")
# node.add_position(26, 2)
# node.display()
#
# print("\n\nAfter deleting the first node")
# node.delete_beginning()
# node.display()
#
# print("\n\nAfter deleting the last node")
# node.delete_end()
# node.display()
#
# print("\n\nAfter deleting the 2nd node")
# node.delete_position(1)
# node.display()

# node1 = LinkedList()
# node2 = LinkedList()
# node3 = LinkedList()
#
# node1.add_tail(2)
# node1.add_tail(4)
# node1.add_tail(7)
# node1.add_tail(1)
#
# node2.add_tail(9)
# node2.add_tail(4)
# node2.add_tail(5)
#
# print(node3.sumOfLinkedLists(node1,node2))
