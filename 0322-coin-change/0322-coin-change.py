from functools import cache
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        n = len(coins)

        dp = [float('inf')]*(amount+1) 
        dp[0] = 0

        for i in range(1,amount+1):
            for c in coins:
                if i - c >= 0:
                    dp[i] = min(dp[i],1+dp[i-c])
        ANS = dp[amount]
        return  ANS if ANS != float('inf') else -1
            
            