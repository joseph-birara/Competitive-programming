class Solution:
    def numSquares(self, n: int) -> int:
        
        nums = []
        if n== 1:
            return 1
        for i in range((n//2) +1):
            if i*i > n:
                break
            nums.append(i*i)
        min_dp = [float(inf)] *( n+1)
        min_dp[0] = 0
        
        for i in range(1,n+1):                   
            for num in nums:
                if i >= num:
                    min_dp[i] = min(min_dp[i], 1+ min_dp[i-num] )
        
        
        if min_dp[-1]==float(inf):
            return -1
                    
        
        return min_dp[-1]
        