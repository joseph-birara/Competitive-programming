class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        total = sum(nums)
        n = len(nums)
        less = 0

        for i in range(n):
            temp = nums[i]
            left = abs(nums[i]*i - less)
            right = abs(nums[i] * (n - i) -( total - less))
            nums[i] = left + right
            less += temp
        return nums
        