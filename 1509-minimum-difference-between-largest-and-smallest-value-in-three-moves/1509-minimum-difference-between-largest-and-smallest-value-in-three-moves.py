class Solution:
    def minDifference(self, nums: List[int]) -> int:
        n = len(nums)
        if n <5:
            return 0       
        
        nums.sort()
       
        for i in range(3):
            left = nums[3-i] - nums[0]
            right = nums[-1] - nums[-4 + i]
            if left > right :
                nums.pop(0)
                
            else:
                nums.pop()
                
        return max(nums)- min(nums)
        