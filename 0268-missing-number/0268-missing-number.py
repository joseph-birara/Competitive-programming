class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for number in range(0,len(nums)+1):
            if number not in nums:
                return number
        