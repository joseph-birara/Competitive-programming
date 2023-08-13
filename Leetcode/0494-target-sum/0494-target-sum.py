class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        
        memo = {}
        def dp(index, summ):
            if index == len(nums):
                return 1 if summ == target else 0
            if (index,summ) in memo:
                return memo[(index,summ)]
            
            memo[(index,summ)] = dp(index+1, summ+nums[index])+ dp(index+1, summ- nums[index])
            return memo[(index,summ)]
            
        
        
        return dp(0,0)
        