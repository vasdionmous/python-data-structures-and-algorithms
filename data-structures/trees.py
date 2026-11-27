# binary tree = each node has <= 2 children
# perfect binary tree = every node has exactly two children
# binary search tree = each internal node is > than all the keys in the (respective) node's LEFT subtree and < the ones in its RIGHT subtree
# BST of heigh h => search, remove and add is O(logh)
# O(logn) = divide and conquer
# a path which is essentially a sorted linked list
# lookup: BST > ll
# remove: BST > ll
# insert: ll > BST
# interview que: add data to a data structure quickly but we don't care about retrieving data: linked list > BST


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    # creates a BST (or any other data for that matter) with a value already in it
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.root = new_node
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        # case: empty tree
        if self.root is None:
            self.root = new_node
            return True

        temp = self.root
        while True:
            # comparing equal values
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                # the spot is empty
                if temp.left is None:
                    temp.left = new_node
                    return True
                # moving temp to continue the loop
                temp = temp.left
            else:
                # same code mirrored
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False
