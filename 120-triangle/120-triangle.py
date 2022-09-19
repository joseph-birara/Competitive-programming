class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        dp = [0]* (len(triangle)+1)
        for row in triangle[::-1]:
            for ind , val in enumerate(row):
                
                dp[ind] = val + min(dp[ind],dp[ind+1])
        
        return dp[0]
                
            
            
        
        