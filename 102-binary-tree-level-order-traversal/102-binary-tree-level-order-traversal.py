# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return None

        d = {}
        self.depthCalculator(root, 0, d)

        result = []

        for key in d:
            result.append(d[key])
        
        return result

    # Helper function
    def depthCalculator(self, root, depth, d):

        if not root:
            return None

        if depth not in d:
            d[depth] = [root.val]

        else:
            d[depth].append(root.val)

        self.depthCalculator(root.left, depth + 1, d)
        self.depthCalculator(root.right, depth + 1, d)