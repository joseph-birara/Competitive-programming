import numpy as np
class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = int(len(nums)//2)
        temp = [nums[i] + nums[-(i+1)] for i in range(n)]
        return np.max(temp)
        