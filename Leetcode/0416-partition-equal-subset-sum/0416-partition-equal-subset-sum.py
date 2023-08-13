class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        total = sum(nums)
        
        if total % 2 !=0 :
            return False
        half = total //2
        
        @cache
        
        def dp(index, curr_sum):
            if index >= len(nums):
                return curr_sum == half
            if curr_sum > half :
                return False
            return dp(index+1 , curr_sum + nums[index]) or dp(index+1 , curr_sum)
        return dp(0, 0)
            
        