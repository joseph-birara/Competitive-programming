class Solution:
    def longestSubarray(self, nums: List[int]) -> int:

        n = len(nums)
        target = max(nums)

        length = 1
        temp_len = 0

        for i in range(n):
            if nums[i] == target:
                temp_len +=1
            else:
                length = max(length, temp_len)
                temp_len = 0
            
        return max(length,temp_len)


        