'''
BINARY SEARCH TREE

1. Check if the tree is BST
2. Find the minimum and maximum values

SOLUTION: O(logn)
'''

# Node Class
from random import randint


class Node():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Binary Tree
def insertIntoTree(root, key):
    if root is None:
        return Node(key)
    side  = randint(0,1)
    if side == 0:
        root.left = insertIntoTree(root.left, key)
    else:
        root.right = insertIntoTree(root.right, key)
    return root

# Binary Search Tree
def insertIntoBst(root, key):
    if root is None:
        return Node(key)
    if key < root.data:
        root.left = insertIntoBst(root.left, key)
    elif key > root.data:
        root.right = insertIntoBst(root.right, key)
    return root

# Create Tree
def createTree(elements):
    root = Node(elements[0])
    print("Select a Tree to be created: 1. Binary Tree  2. Binary Search Tree")
    choice = int(input())
    print(choice)
    for i in range(1, len(elements)):
        if choice == 1:
            root = insertIntoTree(root, elements[i])
        elif choice == 2:
            root = insertIntoBst(root, elements[i])
    return root

# Inputs
def takeElements():
    number_of_values = int(input("Enter the number of elements inside the tree\n"))
    elements = []
    for i in range(number_of_values):
        print("Enter the element "+str(i+1))
        new_element = int(input())
        elements.append(new_element)
    return elements

# Printing A Tree
def printInorder(root):
    if (root is None):
        return
    printInorder(root.left)
    print(root.data, end=" ")
    printInorder(root.right)

# Check if Tree is BST
def removeNone(nums):
    return [x for x in nums if x is not None]
def isBst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = isBst(node.left)
    is_bst_r, min_r, max_r = isBst(node.right)
    is_bst_node = is_bst_l and is_bst_r and (max_l is None or node.data > max_l) and (min_r is None or node.data < min_r)
    min_val = min(removeNone([ min_l, node.data, min_r]))
    max_val = max(removeNone([ max_l, node.data, max_r]))
    return is_bst_node, min_val, max_val

# Main code
if __name__ == "__main__":
    elements = takeElements()
    root = createTree(elements)
    printInorder(root)
    print(isBst(root))