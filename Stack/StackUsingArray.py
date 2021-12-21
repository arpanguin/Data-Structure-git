class StackUsingArray:
    """Stack implementation using array"""

    def __init__(self, data):
        self._data = data

    def __len__(self):
        """Returns the length of the array"""
        return len(self._data)

    def is_empty(self):
        """Returns if stack is empty"""
        is_empty = len(self._data) == 0
        if is_empty:
            print("Stack is empty")
        return is_empty

    def push(self, element):
        """Pushing elements in stack and returns the pushed element"""
        self._data.append(element)
        return element

    def pop(self):
        """Popping last elements in stack and returns the popped element"""
        if not self.is_empty():
            return self._data.pop()

    def top(self):
        """Returns the top most elements in stack"""
        if not self.is_empty():
            return self._data[-1]

    def display(self):
        """Displaying the elements in stack"""
        if not self.is_empty():
            print(self._data)


data = [22, 33, 44]
stack = StackUsingArray(data)

print(f"Stack: ")
stack.display()

print(f"\nPopped element : {stack.pop()}")
stack.display()

print(f"\nPushed element : {stack.push(55)}")
stack.display()

print(f"\nTop element : {stack.top()}")
stack.display()

print("\nAfter Pop: ")
stack.pop()
stack.display()
stack.pop()
stack.display()
stack.pop()
stack.display()
