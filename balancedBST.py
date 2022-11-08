'''
BALANCED BINARY SEARCH TREE

SOLUTION: 
Insert - O(n)
find - O(logn)
update - O(logn)
print - O(n)
'''

# Node BST Class
class nodeBst():
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

def makeBalancedBST(data, lo=0, hi=None, parent=None):
    if hi is None:
        hi = len(data)-1
    if lo>hi:
        return None
    mid = (lo+hi)//2
    key, value = data[mid]
    root = nodeBst(key,value)
    root.parent = parent
    root.left = makeBalancedBST(data, lo, mid-1, root)
    root.right = makeBalancedBST(data, mid+1, hi, root)
    return root

# Printing A Tree
def printInorder(root):
    if (root is None):
        return
    printInorder(root.left)
    print(root.key, end=" ")
    printInorder(root.right)

def printPostorder(root):
    if (root is None):
        return
    printPostorder(root.left)
    printPostorder(root.right)
    print(root.key, end=" ")

def printPreorder(root):
    if (root is None):
        return
    print(root.key, end=" ")
    printPreorder(root.left)
    printPreorder(root.right)

if __name__ == "__main__":
    #data = [ (5,1), (8,2), (9,3), (10,4), (12,5), (14,6), (15,7), (16,8) ]
    data = [(5,4),(8,2),(9,5),(10,1),(14,3)]
    root = makeBalancedBST(data)
    printInorder(root)
    print()
    printPostorder(root)
    print()
    printPreorder(root)