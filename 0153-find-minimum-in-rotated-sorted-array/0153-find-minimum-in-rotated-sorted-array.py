class Solution:
    def findMin(self, nums: List[int]) -> int:

        left = 0
        right = len(nums) - 1
        result = nums[0]

        while left <= right:

            #Case 1: If subarray is already sorted
            if nums[left] < nums[right]:
                result = min(result, nums[left])
            
            # Case 2: If middle value is small
            middle = (left + right) // 2
            result = min(result, nums[middle])

            # Otherwise
            if nums[middle] >= nums[left]:
                left = middle + 1
            else:
                right = middle - 1
        
        return result
        

























        

#         # Referred Neetcode

#         # Default result to be the first number
#         result = nums[0]

#         # Initialize left and right pointers
#         left = 0
#         right = len(nums) - 1

#         while left <= right:

#             # Case 1: The sub-array is already in a sorted order
#             if nums[left] < nums[right]:
#                 result = min(result, nums[left])
#                 break
        
#             # Case 2:
#             middle = (left + right) // 2
#             # Check if middle value < result and update accordingly
#             result = min(result, nums[middle])

#             # Case 2a: 
#             if nums[middle] >= nums[left]:
#                 # Search right
#                 left = middle + 1
            
#             else:
#                 # Search left
#                 right = middle - 1

#         return result
