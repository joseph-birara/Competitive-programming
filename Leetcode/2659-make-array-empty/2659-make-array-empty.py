class Solution:
    def countOperationsToEmptyArray(self, nums: List[int]) -> int:
        position = {num:index for index, num in enumerate(nums)}
        
        nums.sort()
        operations = n = len(nums)        
        for i in range(1,n):
            if position [nums[i]] < position [nums[i-1]]:
                operations += n- i
        return operations
                
        