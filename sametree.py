from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        # recursive step
        return (self.isSameTree(p.left, q.left) and
                self.isSameTree(p.right , q.right))
        
        





#what i tried
# class Solution:
#     def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
#         res1 = []
#         res2 = []

#         def inorder(p, q):
#             if not p and q:
#                 return 
#             inorder(p.left, q.left)
#             res1.append(p.val)
#             res2.append(q.val)
#             inorder(p.right)
#             inorder(q.right)
#         inorder(p, q)
#         return res1 == res2
    
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)

# root1 = TreeNode(1)
# root1.left = TreeNode(2)
# root1.right = TreeNode(3)
    

# s = Solution()
# print(s.isSameTree(root, root1))