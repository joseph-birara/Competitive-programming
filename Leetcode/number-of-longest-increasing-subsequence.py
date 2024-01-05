from typing import List
from collections import Counter

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n

        # dp[i][0] represents the length of LIS ending at position i
        # dp[i][1] represents the count of LIS ending at position i
        dp = [[1, 1] for _ in range(n)]

        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    if dp[i][0] == dp[j][0] + 1:
                        dp[i][1] += dp[j][1]
                    elif dp[i][0] < dp[j][0] + 1:
                        dp[i] = [dp[j][0] + 1, dp[j][1]]

        max_length = max(dp[i][0] for i in range(n))
        return sum(dp[i][1] for i in range(n) if dp[i][0] == max_length)

