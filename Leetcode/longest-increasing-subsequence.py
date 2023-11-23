class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0
        dp = [1]*n 
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i],dp[j] +1 )
        return max(dp)
        
        # @cache
        # def dp(prev, index, length):
        #     if index == n:
        #         return length
        #     if nums[prev] < nums[index]:
        #         include = dp(index,index+1,length+1)
        #         exclude = dp(prev,index+1,length)
        #         return max(include,exclude)
        #     else:
        #         exclude = dp(prev,index+1,length)
        #         start = dp(index,index+1,1)
        #         return max(start,exclude)
        # return dp(0,1,1)
        
        