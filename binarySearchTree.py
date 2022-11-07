'''
BINARY SEARCH TREE

1. Create 2 trees - one is BST 
2. Check if the trees are BST
3. Find the minimum and maximum values
4. Find an element

SOLUTION: O(logn)
'''

from random import randint

# Node Tree Class
class nodeTree():
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# Binary Tree
def insertIntoTree(node, key):
    if node is None:
        return nodeTree(key)
    side  = randint(0,1)
    if side == 0:
        node.left = insertIntoTree(node.left, key)
    else:
        node.right = insertIntoTree(node.right, key)
    return node

# Node BST Class
class nodeBst():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

# Binary Search Tree
def insertIntoBst(node, key, value):
    if node is None:
        node = nodeBst(key, value)
    if key < node.key:
        node.left = insertIntoBst(node.left, key, value)
        node.left.parent = node
        print(node.left.parent)
    elif key > node.key:
        node.right = insertIntoBst(node.right, key, value)
        node.right.parent = node
        print(node.right.parent)
    return node

# Create Tree
def createTree(keys, values):
    print("Select a Tree to be created: 1. Binary Tree  2. Binary Search Tree")
    choice = int(input())
    print(choice)
    root = None
    for i in range(0, len(keys)):
        if choice == 1:
            root = insertIntoTree(root, keys[i])
        elif choice == 2:
            root = insertIntoBst(root, keys[i], values[i])
    return root

# Inputs
def takeElements():
    number_of_elements = int(input("Enter the number of elements inside the tree\n"))
    keys = []
    values = []
    for i in range(number_of_elements):
        print("Enter the key "+str(i+1))
        keys.append(int(input()))
        print("Enter the value "+str(i+1))
        values.append(int(input()))
    return keys, values

# Printing A Tree
def printInorder(root):
    if (root is None):
        return
    printInorder(root.left)
    print(root.key, end=" ")
    printInorder(root.right)

# Check if Tree is BST
def removeNone(nums):
    return [x for x in nums if x is not None]
def isBst(node):
    if node is None:
        return True, None, None
    is_bst_l, min_l, max_l = isBst(node.left)
    is_bst_r, min_r, max_r = isBst(node.right)
    is_bst_node = is_bst_l and is_bst_r and (max_l is None or node.key > max_l) and (min_r is None or node.key < min_r)
    min_val = min(removeNone([ min_l, node.key, min_r]))
    max_val = max(removeNone([ max_l, node.key, max_r]))
    return is_bst_node, min_val, max_val

# find a node in BST
def findNode(node, key):
    if node is None:
        return None
    if key == node.key:
        return node
    if key < node.key:
        return findNode(node.left, key)
    if key > node.key:
        return findNode(node.right, key)

# Check if tree is balanced
def isBalanced(node):
    if node is None:
        return True, 0
    bal_l, height_l = isBalanced(node.left)
    bal_r, height_r = isBalanced(node.right)
    bal = bal_l and bal_r and abs(height_l - height_r)<=1
    height = 1+max(height_l, height_r)
    return bal, height

# Main code
if __name__ == "__main__":
    keys, values = takeElements()
    root = createTree(keys, values)
    printInorder(root)
    print(isBst(root))
    node = findNode(root, 12)
    print(node.key, node.value, node.parent.key)
    print(isBalanced(root))