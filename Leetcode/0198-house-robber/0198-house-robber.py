from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:  # Handle empty list
            return 0
        if len(nums) == 1:  # Handle single house case
            return nums[0]

        memo = {}

        def recur(i):
            if i == 0:  # Base case: First house
                return nums[0]
            if i == 1:  # Base case: Second house
                return max(nums[0], nums[1])

            if i not in memo:  # If result not already computed
                memo[i] = max(recur(i - 2) + nums[i], recur(i - 1))  # Rob or skip
            return memo[i]

        return recur(len(nums) - 1)  # Start from the last house
