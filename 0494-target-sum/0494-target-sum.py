class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        @cache
        def dp(ind,total):
            if ind == len(nums):
                if total == target :
                    return 1
                return 0
            
            return dp(ind+1,total+ nums[ind]) +  dp(ind+1,total-nums[ind])
        return dp(0,0)