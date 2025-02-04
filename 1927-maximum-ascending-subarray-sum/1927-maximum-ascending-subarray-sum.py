class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        inc = nums[0]
        max_sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]: 
                inc += nums[i] 
            else:
                inc = nums[i]          
           

            max_sum = max(max_sum, inc)
        return max_sum