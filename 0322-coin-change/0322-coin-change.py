class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        
        
        min_dp = [float(inf)] *( amount+1)
        min_dp[0] = 0
        
        for i in range(1,amount+1):                   
            for coin in coins:
                if i >= coin:
                    min_dp[i] = min(min_dp[i], 1+ min_dp[i-coin] )
        
        
        if min_dp[-1]==float(inf):
            return -1
                    
        
        return min_dp[-1]
        
        
        
        
        