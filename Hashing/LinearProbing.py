class LeanerProbing:
    def __init__(self):
        self.length = 10
        self.hashtable = [-1] * self.length
        self.size = 0

    def is_empty(self):
        """Checking if hash table is empty"""
        return self.size == 0

    def insert(self, element):
        """Inserting the element into hash table
            i. finding the hash value
            ii. checking if the index(i.e. hash value) is present in array or else incrementing by 1
            iii. inserting the element
        """
        if type(element) != int:
            raise TypeError("Element is not an integer")
        if (self.size * 2) == self.length:
            raise IndexError("HashTable is full")

        hash_value = element % self.length
        while self.hashtable[hash_value] != -1:
            hash_value += 1
        self.hashtable[hash_value] = element
        self.size += 1

    def search(self, element):
        if type(element) != int:
            raise TypeError("Element is not an integer")

        hash_value = element % self.length
        try:
            while self.hashtable[hash_value] != element:
                hash_value += 1
        except IndexError as error:
            hash_value = 0
        return hash_value or -1

    def display(self):
        """Displaying the element of hash table"""
        for i in range(self.length):
            print(f"[{i}] ==> {self.hashtable[i]}")


linear_probing = LeanerProbing()
linear_probing.insert(12)
linear_probing.insert(13)
linear_probing.insert(42)
linear_probing.insert(48)
linear_probing.insert(99)
#linear_probing.insert(52)
linear_probing.display()
print(linear_probing.search(99))
