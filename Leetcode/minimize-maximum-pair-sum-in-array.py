class Solution:
    def minPairSum(self, nums: List[int]) -> int:

        nums.sort()
        res = 0

        left = 0
        right = len(nums) - 1
        while left <right:
            curr = nums[left] + nums[right]
            res = max(res,curr)
            left += 1
            right -=1 
        return res
        