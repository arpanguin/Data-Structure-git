from LinkedList.SimpleLinkedList import LinkedList


class Chaining:
    def __init__(self):
        self.size = 10
        self.hashtable = [0] * self.size
        for i in range(self.size):
            self.hashtable[i] = LinkedList()

    def insert(self, element):
        """inserting element in hash table through chaining mechanism
            i. Finding the index using mod function
            ii. Creating linked list and added at last in sorted order
        """
        if type(element) != int:
            raise TypeError("Element is not an integer")
        mod_index = element % self.size  # Finding the mod index to start the chain
        self.hashtable[mod_index].insert_sorted(element)

    def search(self, key):
        """Returns the index of key from linked list
            :return index from 0 to 1 or -1
        """
        if type(key) != int:
            raise TypeError("key is not an integer")
        hash_value = key % self.size
        return self.hashtable[hash_value].search(key)

    def display(self):
        """Displaying the hash table"""
        for i in range(self.size):
            print(f"[{i}] ==> ", end="")
            self.hashtable[i].display()
            print()


chain = Chaining()
chain.insert(14)
chain.insert(42)
chain.insert(22)
chain.insert(32)
chain.insert(44)
chain.insert(46)
chain.insert(54)
chain.insert(52)
chain.insert(100)
chain.insert(101)
print(f"Element position : {chain.search(32)}")
chain.display()
