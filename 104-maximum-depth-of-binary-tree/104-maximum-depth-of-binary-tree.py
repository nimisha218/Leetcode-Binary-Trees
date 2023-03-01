# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        # ----------------------------------------------------------------------------

        # Approach 1 -> Recursive DFS -> return 1 + max(left_subtree, right_subtree)

        # Base case:
        if root == None:
            return 0
        
        # Recursive case
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

        # ----------------------------------------------------------------------------

        # # Approach 2 -> BFS -> Using a queue

        # # Base case:
        # if root == None:
        #     return 0
        
        # level = 0

        # q = deque([root])

        # while q:
            
        #     for i in range(len(q)):
        #         node = q.popleft()
        #         if node.left != None:
        #             q.append(node.left)
        #         if node.right != None:
        #             q.append(node.right)
            
        #     level = level + 1
        
        # return level

        # ----------------------------------------------------------------------------

        # # Approach 3 -> Iterative DFS -> Using a stack

        # # Base Case:
        # if root == None:
        #     return 0
        
        # stack = [[root, 1]]

        # result = 1

        # while stack:

        #     node, depth = stack.pop()
            
        #     if node:
        #         result = max(result, depth)
        #         stack.append([node.left, 1+depth])
        #         stack.append([node.right, 1+depth])
        
        # return result

        # ----------------------------------------------------------------------------

        # Approach 4 -> What we tried initially


        # if not root:
        #     return 0

        # left_depth_count = 1
        # right_depth_count = 1

        

        # left_depth = Solution().calculateLeftDepth(root.left,left_depth_count)
        # right_depth = Solution().calculateRightDepth(root.right,right_depth_count)

        # print("Left Depth: ", left_depth)
        # print("Right Depth: ", right_depth)

        # if left_depth > right_depth:
        #     return left_depth
        # else:
        #     return right_depth

    # def calculateLeftDepth(self, root, left_depth_count):
        
    #     if not root:
    #         return left_depth_count

    #     else:
    #         left_depth_count = left_depth_count + 1
    #         l = Solution().calculateLeftDepth(root.left,left_depth_count)
    #         r = Solution().calculateRightDepth(root.right,left_depth_count)

    #         if l > r:
    #             return l
    #         else:
    #             return r
        
        
        
    # def calculateRightDepth(self, root, right_depth_count):
        
    #     if not root:
    #         return right_depth_count

    #     else:
    #         right_depth_count = right_depth_count + 1
    #         l = Solution().calculateLeftDepth(root.left,right_depth_count)
    #         r = Solution().calculateRightDepth(root.right,right_depth_count)

    #         if l > r:
    #             return l
    #         else:
    #             return r

    # ----------------------------------------------------------------------------
        
