class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1

        while left <= right:

            middle = (left + right) // 2

            if nums[middle] == target:
                return middle

            if nums[left] <= nums[middle]:
                if nums[middle] < target or target < nums[left]:
                    left = middle + 1
                else:
                    right = middle - 1
            
            else:
                if target < nums[middle] or nums[right] < target:
                    right = middle - 1
                else:
                    left = middle + 1
            
        return -1   












        


