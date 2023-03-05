# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        if not root:
            return
        
        l = []

        self.all_nodes(root, l)

        l.sort()

        return l[k-1]
    
    def all_nodes(self, node, l):

        if not node:
            return
        
        l.append(node.val)

        self.all_nodes(node.left, l)
        self.all_nodes(node.right, l)


        