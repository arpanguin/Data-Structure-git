class Heaps:
    def __init__(self):
        self._max_size = 10
        self._current_size = 0
        self.data = [-1] * (self._max_size + 1)

    def insert(self, element):
        """Inserting element in heap or priority queue"""
        if self._current_size == self._max_size:
            print("Queue is full")
            return
        self._current_size += 1
        position = self._current_size

        while position > 1 and element > self.data[position // 2]:
            """[position // 2] used to find the parent node"""
            """Comparing element with parent node and swapping the data"""
            self.data[position] = self.data[position // 2]
            position //= 2
        self.data[position] = element

    def delete(self):
        """Delete the first element or max element from heap and replace with the last element
            Then check if root element is smaller than any child element then replace with the max child
        """
        element_to_remove = self.data[1]
        self.data[1] = self.data[self._current_size]
        self.data[self._current_size] = -1
        self._current_size -= 1
        root_node = 1
        left_node = root_node * 2
        right_node = left_node + 1

        while left_node <= self._current_size:  # Checking if it reaches to leaf node then stop the loop
            max_node = left_node if self.data[left_node] > self.data[right_node] else right_node
            if self.data[root_node] < self.data[max_node]:  # Checking the max child node with root node
                temp = self.data[root_node]
                self.data[root_node] = self.data[max_node]
                self.data[max_node] = temp
            root_node = max_node
            left_node = root_node * 2
            right_node = left_node + 1
        return element_to_remove

    def max(self):
        """Returns the highest element from heap"""
        if self._current_size > 0:
            return self.data[1]

    def display(self):
        """Display the heap"""
        [print(self.data[i], end="-->") for i in range(1, self._current_size + 1)]


heaps = Heaps()
# heaps.insert(11)
# heaps.insert(9)
# heaps.insert(7)
# heaps.insert(5)
# heaps.insert(8)
# heaps.insert(3)

heaps.insert(11)
heaps.insert(5)
heaps.insert(7)
heaps.insert(3)
heaps.insert(4)
heaps.insert(6)
heaps.display()
print(f"\n\nHighest number : {heaps.max()}")
print(f"\n\nRemoved element : {heaps.delete()}")
heaps.display()
print(f"\n\nRemoved element : {heaps.delete()}")
heaps.display()
