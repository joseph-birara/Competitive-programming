from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()
        low, high = 0, nums[-1] - nums[0]
        
        while low < high:
            mid = (low + high) // 2
            if self.countPairs(nums, mid) < k:
                low = mid + 1
            else:
                high = mid
        
        return low

    def countPairs(self, nums: List[int], max_distance: int) -> int:
        count = left = 0
        for right in range(1, len(nums)):
            while nums[right] - nums[left] > max_distance:
                left += 1
            count += right - left
        return count
