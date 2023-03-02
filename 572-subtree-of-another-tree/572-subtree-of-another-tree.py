# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if not subRoot:
            return True
        
        if not root:
            return False
        
        if self.isSameTree(root, subRoot) == True:
            return True
        
        else:
            return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
            
    
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # ---------------------------------------------------------------------------

        # Recursive DFS Approach:

        # Base Case 1: Check if both the trees are empty -> return True
        if not p and not q:
            return True

        # Base Case 2: Check if one of the trees is empty -> return False
        if not p or not q:
            return False

        # Base Case 3: Check if the val at the nodes is the same or not
        if p.val != q.val:
            return False
        
        # Recursive Case: Recursively check for the left and right sub-tree
        return (self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right))
        
        







        
        