#data structure that has at most 2 child nodes

# Fast search, insert, delete(O(log n))
# sorted data
# hierarchy modeling parent-child relationships

# Use cases
# storing time-series data: energy production per-hour. 
# optimized queries: find max output between 2-4pm
# Organize sensor hierarchies: If you have panels → strings → inverters, a tree mirrors this structure naturally.


# Binary Tree Visualization/simulation
# https://www.cs.usfca.edu/~galles/visualization/BST.html

class TreeNode:
    
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else:
                self.right.insert(value)
                
                
    # Inorder : Left -> Root -> Right 
    # go left as deep as possible, print when returning, then go right           
    def inorder_traversal(self): 
        if self.left:
            self.left.inorder_traversal()
        print(self.value)
        if self.right:
            self.right.inorder_traversal()
            
            
            
    # Preorder : Root -> Left -> Right
    #print first, the go left as deep as possible, then right.
    def preorder_traversal(self): 
        print(self.value)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

            
    # Postorder : Left -> Right -> Root
    # Go deep left, then deep right, print each node only after both children are done.
    def postorder_traversal(self): 
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
            
            
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            return True


                
                
                
                
                
                
                
                
                
tree = TreeNode(10)
tree.insert(5)
tree.insert(4)
tree.insert(7)
tree.insert(1)
tree.insert(12)
tree.insert(11)
tree.insert(22)

# print(tree.find(3))
# print(tree.find(22))
# print('inord')
# tree.inorder_traversal()  
# print('inord')
# print('pree')
# tree.preorder_traversal()
# print('pree')
# print('post')
# tree.postorder_traversal()
# print('post')
# print(tree.left.right.value) #7
        