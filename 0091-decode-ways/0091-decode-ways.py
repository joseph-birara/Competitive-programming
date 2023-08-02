class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        
        for i in range(1, n + 1):
            # Check if s[i-1:i] is a valid one-digit number
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]
            
            # Check if s[i-2:i] is a valid two-digit number
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]
        
        return dp[n]
