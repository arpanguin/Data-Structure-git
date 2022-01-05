class Node:
    __slots__ = '_element', '_left', '_right'

    def __init__(self, element, left=None, right=None):
        self._element = element
        self._left = left
        self._right = right


class BinarySearchTree:
    def __init__(self):
        self._root = None

    def insert(self, root_node, element):
        """Inserting the node in binary search tree"""
        temp = None
        while root_node:
            temp = root_node
            if element == root_node._element:
                return
            elif element < root_node._element:
                root_node = root_node._left
            else:
                root_node = root_node._right
        node = Node(element)

        if self._root:
            if element < temp._element:
                temp._left = node
            else:
                temp._right = node
        else:
            self._root = node

    def search(self, element):
        """searching element position, number of traversal required and path
        :return position, no_of_traversal, path
        """
        print(self._root._element)
        pass

    def delete(self, root_node, element):
        """Deleting a node"""

    def display_preorder(self, root_node):
        """root, left, right"""
        if root_node:
            print(root_node._element, end="-->")
            self.display_preorder(root_node._left)
            self.display_preorder(root_node._right)

    def display_inorder(self, root_node):
        """left, root, right, always returns in sorted order"""
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


    def findClosestValueInBst(self, tree, target):
        # Write your code here.
        closest_val = self.find_val(tree, tree, target)
        print(closest_val)


    def find_val(self, current_node, tree, target):
        diff = current_node._element - target
        if target > current_node._element and abs(diff) > abs(target - current_node._right._element):
            return current_node._right.value
        elif target > current_node._element:
            self.find_val(current_node._right, tree, target)
        elif target < current_node._element and abs(diff) < abs(target - current_node._left._element):
            return current_node._left._element
        elif target < current_node._element:
            self.find_val(current_node._left, tree, target)
        else:
            return current_node

    def isBST(self, root):
        if root:
            return True
        if self.isBST(root._left) == False:
            return False
        if root.data <= prev:
            return false
        prev = root.data
        return self.isBST(root._right)

tree = BinarySearchTree()
tree.insert(tree._root, 2)
tree.insert(tree._root, 1)
tree.insert(tree._root, 3)
# tree.insert(tree._root, 3)
# tree.insert(tree._root,2)
# tree.insert(tree._root,5)
# tree.insert(tree._root,1)
# tree.insert(tree._root,4)
print(tree.isBST(tree._root))
# print("Pre-order.....")
# tree.display_preorder(tree._root)
#
# print("\n\nIn-order.....")
# tree.display_inorder(tree._root)
#
# print("\n\nPost-order.....")
# tree.display_postorder(tree._root)
#
# print("\n\nsearch:")
# tree.search(4)