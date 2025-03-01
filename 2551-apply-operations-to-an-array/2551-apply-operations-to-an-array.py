class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)

        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] *=2
                nums[i+1] = 0
        
        left = 0

        for i in range(n):
            while left < i and nums[left] != 0 :
                left += 1
            if nums[left] == 0 and nums[i] != 0:
                nums[left] , nums[i] = nums[i] , nums[left]
        return nums
        