# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # ---------------------------------------------------------------------------

    

    # ---------------------------------------------------------------------------
    
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


        # ---------------------------------------------------------------------------

    #     if p == None and q == None:
    #         return True
        
    #     if p == None and q != None:
    #         return False

    #     if q == None and p != None:
    #         return False

    #     # Let's try getting the preorder right
    #     # Root, Left, Right
    #     tree1 = []
    #     tree2 = []

    #     tree1.append(p.val)
    #     if p.left != None:
    #         Solution().traverseTreeInorder(p.left, tree1)
    #     else:
    #         tree1.append('null')
    #     if p.right != None:
    #         Solution().traverseTreeInorder(p.right, tree1)
    #     else:
    #         tree1.append('null')
        
    #     tree2.append(q.val)
    #     if q.left != None:
    #         Solution().traverseTreeInorder(q.left, tree2)
    #     else:
    #         tree2.append('null')
    #     if q.right != None:
    #         Solution().traverseTreeInorder(q.right, tree2)
    #     else:
    #         tree2.append('null')
        
    #     if tree1 != tree2:
    #         return False
        
        

    #     # Post Order
    #     # Left, Right, Root
    #     tree1 = []
    #     tree2 = []

    #     if p.left != None:
    #         Solution().traverseTreePostorder(p.left, tree1)
    #     else:
    #         tree1.append('null')
    #     if p.right != None:
    #         Solution().traverseTreePostorder(p.right, tree1)
    #     else:
    #         tree1.append('null')
    #     tree1.append(p.val)

    #     if q.left != None:
    #         Solution().traverseTreePostorder(q.left, tree2)
    #     else:
    #         tree2.append('null')
    #     if q.right != None:
    #         Solution().traverseTreePostorder(q.right, tree2)
    #     else:
    #         tree2.append('null')
    #     tree2.append(q.val)

    #     if tree1 != tree2:
    #         return False

    #     # Pre order
    #     # Left, Root, Right

    #     tree1 = []
    #     tree2 = []

    #     if p.left != None:
    #         Solution().traverseTreePostorder(p.left, tree1)
    #     else:
    #         tree1.append('null')
    #     tree1.append(p.val)
    #     if p.right != None:
    #         Solution().traverseTreePostorder(p.right, tree1)
    #     else:
    #         tree1.append('null')
        
    #     if q.left != None:
    #         Solution().traverseTreePostorder(q.left, tree2)
    #     else:
    #         tree2.append('null')
    #     tree2.append(q.val)
    #     if q.right != None:
    #         Solution().traverseTreePostorder(q.right, tree2)
    #     else:
    #         tree2.append('null')
        
    #     if tree1 != tree2:
          
    #         return False

    #     return True

        

    # def traverseTreeInorder(self, root, tree1):

    #     tree1.append(root.val)

    #     if root.left != None:
    #         Solution().traverseTreeInorder(root.left, tree1)
    #     else:
    #         tree1.append('null')
        
        
    #     if root.right != None:
    #         Solution().traverseTreeInorder(root.right, tree1)
    #     else:
    #         tree1.append('null')

    #     return 

    # def traverseTreePostorder(self, root, tree1):

    #     if root.left != None:
    #         Solution().traverseTreeInorder(root.left, tree1)
    #     else:
    #         tree1.append('null')
        
    #     if root.right != None:
    #         Solution().traverseTreeInorder(root.right, tree1)
    #     else:
    #         tree1.append('null')
        
    #     tree1.append(root.val)

    #     return

    # def traverseTreePreorder(self, root, tree1):

    #     if root.left != None:
    #         Solution().traverseTreeInorder(root.left, tree1)
    #     else:
    #         tree1.append('null')
        
    #     tree1.append(root.val)
    
    #     if root.right != None:
    #         Solution().traverseTreeInorder(root.right, tree1)
    #     else:
    #         tree1.append('null')

    #     return
