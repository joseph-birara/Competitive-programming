

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left = 0
        n = len(nums)
        d = defaultdict(int)   
        res = 0     

        for right in range(n):
            d[nums[right]] += 1            
            while d[0] > k:
                d[nums[left]] -= 1
                left += 1
            factor = right - left + 1
            res = max(factor, res)
        return res
