class Solution:
    def minIncrementForUnique(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        res = 0
        for i in range(1,n):
            if nums[i-1] >= nums[i]:
                res += (nums[i-1] - nums[i]) + 1
                nums[i] = nums[i-1] + 1
        return res
        