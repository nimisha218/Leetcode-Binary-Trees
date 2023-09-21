import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        result = right

        while left <= right:
            middle = (left + right) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(p/middle)
            if hours <= h:
                result = min(result, middle)
                right = middle - 1
            else:
                left = middle + 1
        
        return result










        # max_piles = max(piles)
        # print("Max of piles: ", max_piles)

        # possible_solutions = [i for i in range(1,max_piles+1)]    
        # print("Possible solutions: ", possible_solutions)

        # # Start our binary search approach
        # left = 0
        # right = len(possible_solutions) - 1

        # flag = 0
        # while left <= right:
        #     print("Left: ", left)
        #     print("Right: ", right)
        #     middle = (left + right) // 2
        #     print("Middle: ", middle)
        #     # Check if we have a solution with middle value
        #     check = possible_solutions[middle]
        #     print("Checking for: ", check)
        #     hours = 0
        #     for i in range(len(piles)):
        #         eat = math.ceil(piles[i]/check)
        #         hours += eat
        #     print("Total hours required: ", hours)
        #     if hours <= h:
        #         if hours == h:
        #             temp = possible_solutions[middle]
        #             flag = 1
        #         print("Decrease")
        #         right = middle - 1
        #         print("Left: ", left)
        #         print("Updated right: ", right)
        #     else:
        #         print("Increase")
        #         # print("Updated middle, ", middle)
        #         left = middle + 1
        #         print("Updated left: ", left)
        #         print("right: ", right)
            
        # if flag == 1 and left > right:
        #     return temp

        # return possible_solutions[middle]