class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        n = len(nums)

        for index in range(1,n):
            nums[index] += nums[index-1]
        count = 0

        for i in range(n-1):
            if nums[i] >= nums[-1] - nums[i]:                
                count += 1
        return count
        