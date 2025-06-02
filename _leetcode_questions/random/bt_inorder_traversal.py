#Recursive version
from typing import List, Optional


class TreeNode:
        # Constructor to initialize a TreeNode  
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Recursive:
    # Method to perform inorder traversal on a binary tree and return the result as a list
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]

        # Helper/nested function that performs the actual recursive traversal
        def inorder(root):
            if not root: # base case
                return
            inorder(root.left) # recursively visits left
            res.append(root.val) 
            inorder(root.right) # recursively visits right

        inorder(root)
        return res
    

# this is an instance. root is an object that holds the 
#instance. this is manually creating binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

s = Recursive()
print(s.inorderTraversal(root))

# iteration version
class Iterative:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res =[]
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            res.append(cur.val)
            cur = cur.right
        return res
    
i = Iterative()
print(i.inorderTraversal(root))