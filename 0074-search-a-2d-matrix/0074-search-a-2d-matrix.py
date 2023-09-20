class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        num_rows = len(matrix)
        num_cols = len(matrix[0])

        count = 0

        i = 0

        while count < num_rows:

            # Check for satisfaction of first row
            if matrix[i][0] <= target and matrix[i][-1] >= target:
                # Row found!
                # print("Row identified: ", matrix[i])
                # Starting binary search here
                left = 0
                right = num_cols - 1
                while left <= right:
                    middle = (left + right) // 2
                    if matrix[i][middle] == target:
                        return True
                    elif matrix[i][middle] < target:
                        left = middle + 1
                    else:
                        right = middle - 1
                return False
            else:
                i = i + 1
            count += 1
        
        return False
