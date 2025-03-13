from typing import List

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        size = len(nums)
        low, high = 0, len(queries)

        if not self.canMakeZero(nums, queries, high):
            return -1

        while low <= high:
            mid = low + (high - low) // 2
            if self.canMakeZero(nums, queries, mid):
                high = mid - 1
            else:
                low = mid + 1

        return low

    def canMakeZero(self, nums: List[int], queries: List[List[int]], limit: int) -> bool:
        size = len(nums)
        current_sum = 0
        delta = [0] * (size + 1)

        for i in range(limit):
            start, end, value = queries[i]
            delta[start] += value
            delta[end + 1] -= value

        for j in range(size):
            current_sum += delta[j]
            if current_sum < nums[j]:
                return False
        return True
