class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        import math
        start, end = 1, max(nums)
        while start < end:
            mid = start + (end - start) // 2
            SUM = sum(ceil(num / mid) for num in nums)
            if threshold < SUM:
                start = mid + 1
            else:
                end = mid       
        return end
                
            
            
        