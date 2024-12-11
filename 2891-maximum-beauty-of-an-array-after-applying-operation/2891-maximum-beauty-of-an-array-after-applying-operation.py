class Solution:
    def maximumBeauty(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        max_len = 0
        start = 0

        for i in range(len(nums)):
            while start < i and nums[start] < nums[i] - 2* k:
                start += 1

            max_len = max(max_len, i - start +1)
        
        return  max_len

        
        

        

        

        