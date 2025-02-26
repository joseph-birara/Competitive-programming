class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        max_sum = current_sum = nums[0] 

    
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])  
            max_sum = max(max_sum, current_sum) 

        min_sum = current_sum = nums[0] 

        for i in range(1, len(nums)):
            current_sum = min(nums[i], current_sum + nums[i])  
            min_sum = min(min_sum, current_sum) 
        
        return max(abs(min_sum), abs(max_sum))

