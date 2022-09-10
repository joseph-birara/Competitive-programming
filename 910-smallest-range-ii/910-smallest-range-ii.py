class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()
        maxE=nums[n-1]
        minE=nums[0]
        ans=maxE-minE
        for i in range(n-1):
            
            currMax = max(nums[n-1] - k, nums[i] + k)
            currMin = min(nums[0] + k, nums[i+1] - k)
            ans = min(ans, currMax - currMin)
        
        return ans
        
        
        