class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(2,n):
            nums[i] += max(nums[:i-1])
        return max(nums)



        