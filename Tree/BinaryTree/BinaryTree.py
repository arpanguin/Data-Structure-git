from Queues.QueueUsingArray import QueueUsingArray as Queue


class Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinaryTree:
    def __init__(self):
        self._root = None

    def make_tree(self, element, left, right):
        """Creating a tree"""
        node = Node(element, left._root, right._root)
        self._root = node

    def display_preorder(self, root_node):
        """root, left, right"""
        if root_node:
            print(root_node._element, end="-->")
            self.display_preorder(root_node._left)
            self.display_preorder(root_node._right)

    def display_inorder(self, root_node):
        """left, root, right"""
        if root_node:
            self.display_inorder(root_node._left)
            print(root_node._element, end="-->")
            self.display_inorder(root_node._right)

    def display_postorder(self, root_node):
        """left, right, root"""
        if root_node:
            self.display_postorder(root_node._left)
            self.display_postorder(root_node._right)
            print(root_node._element, end="-->")

    def display_levelorder(self, root_node):
        """Level by level, left to right, top to bottom"""
        queue = Queue()
        queue.enqueue(root_node)
        while not queue.is_empty():
            node = queue.dequeue()
            print(node._element, end="-->")
            if node._left:
                queue.enqueue(node._left)
            if node._right:
                queue.enqueue(node._right)

    def count_nodes(self, root_node):
        """Counting the number of nodes"""
        if root_node:
            x = self.count_nodes(root_node._left)
            y = self.count_nodes(root_node._right)
            return x + y + 1
        return 0

    def height(self, root_node):
        """Returns the height of the tree"""
        if root_node:
            x = self.height(root_node._left)
            y = self.height(root_node._right)
            if x > y:
                return x + 1
            else:
                return y + 1
        return 0


null = BinaryTree()
a = BinaryTree()
b = BinaryTree()
c = BinaryTree()
d = BinaryTree()
e = BinaryTree()

a.make_tree("A", null, null)
b.make_tree("B", null, null)
c.make_tree("C", a, b)

d.make_tree("D", null, null)
e.make_tree("E", c, d)

binary_tree = BinaryTree()

print("Pre-order.....")
binary_tree.display_preorder(e._root)

print("\n\nIn-order.....")
binary_tree.display_inorder(e._root)

print("\n\nPost-order.....")
binary_tree.display_postorder(e._root)

print("\n\nLevel-order.....")
binary_tree.display_levelorder(e._root)

print(f"\n\nNumber of Node is ==> {binary_tree.count_nodes(e._root)}")
print(f"\n\nHeight of the tree is ==> {binary_tree.height(e._root)}")
