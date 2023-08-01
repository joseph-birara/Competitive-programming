class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        increasing_length = 1  # Length of the longest wiggle subsequence ending with an increasing difference
        decreasing_length = 1  # Length of the longest wiggle subsequence ending with a decreasing difference
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                increasing_length = decreasing_length + 1
            elif nums[i] < nums[i - 1]:
                decreasing_length = increasing_length + 1
        
        return max(increasing_length, decreasing_length)
