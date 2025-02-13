from typing import List
import heapq

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums) 
        cnt = 0

        while len(nums) >= 2:
            if nums[0] >= k:
                return cnt
            cnt += 1
            x = heapq.heappop(nums)  
            y = heapq.heappop(nums)
            num = 2 * min(x, y) + max(x, y)
            heapq.heappush(nums, num)  

        return cnt if nums and nums[0] >= k else 0  
