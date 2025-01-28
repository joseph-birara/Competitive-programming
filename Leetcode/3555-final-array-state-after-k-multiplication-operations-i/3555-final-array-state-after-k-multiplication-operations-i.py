import heapq
from typing import List

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        
        nums = [(num, index) for index, num in enumerate(nums)]
        heapq.heapify(nums)  

        
        for _ in range(k):
            num, index = heapq.heappop(nums) 
            num *= multiplier  
            heapq.heappush(nums, (num, index)) 

        
        ans = [0] * len(nums)
        for num, index in nums:
            ans[index] = num

        return ans
