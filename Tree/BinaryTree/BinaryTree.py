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

    def branchSums(self, root):
        """Summing up each branch of the tree"""
        total_sum = []
        self.branchSums_helper(root, 0, total_sum)
        return total_sum

    def branchSums_helper(self, node, branch_sum, total_sum):
        """Branch sum helper method"""
        if not node:
            return
        branch_sum += node._element

        if not node._left and not node._right:
            total_sum.append(branch_sum)

        self.branchSums_helper(node._left, branch_sum, total_sum)
        self.branchSums_helper(node._right, branch_sum, total_sum)


null = BinaryTree()
a = BinaryTree()
b = BinaryTree()
c = BinaryTree()
d = BinaryTree()
e = BinaryTree()
f = BinaryTree()
g = BinaryTree()
h = BinaryTree()
i = BinaryTree()
j = BinaryTree()

a.make_tree(8, null, null)
b.make_tree(9, null, null)
c.make_tree(10, null, null)
d.make_tree(4, a, b)
e.make_tree(5, c, null)
f.make_tree(2, d, e)

g.make_tree(6, null, null)
h.make_tree(7, null, null)
i.make_tree(3, g, h)

j.make_tree(1, f, i)

binary_tree = BinaryTree()

print("Pre-order.....")
binary_tree.display_preorder(j._root)

print("\n\nIn-order.....")
binary_tree.display_inorder(j._root)

print("\n\nPost-order.....")
binary_tree.display_postorder(j._root)

print("\n\nLevel-order.....")
binary_tree.display_levelorder(j._root)

print(f"\n\nNumber of Node is ==> {binary_tree.count_nodes(j._root)}")
print(f"\nHeight of the tree is ==> {binary_tree.height(j._root)}")

print("\nBranch Sums.....")
print(binary_tree.branchSums(j._root))
