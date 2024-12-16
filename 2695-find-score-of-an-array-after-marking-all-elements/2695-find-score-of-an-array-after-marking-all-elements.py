from collections import defaultdict
from typing import List

class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Pair each number with its index
        indexed_nums = [(num, index) for index, num in enumerate(nums)]
        
        d = defaultdict(int)  # Dictionary to track used indices
        score = 0

        # Sort the array based on the numbers
        indexed_nums.sort()

        for num, index in indexed_nums:
            # If the index has not already been marked
            if not d[index]:
                score += num
                d[index] = 1
                
                # Mark adjacent indices if they exist
                if index > 0:
                    d[index - 1] = 1
                if index < len(nums) - 1:
                    d[index + 1] = 1

        return score
