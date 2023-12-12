class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        res = -1
        small = min(nums)
        big = max(nums)

        for num in nums:
            if num != small and num != big:
                return num
        return res
        