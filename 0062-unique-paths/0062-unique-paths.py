from functools import cache

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        @cache
        def dp(row, col):
            
            if row == 0 and col == 0:
                return 1
            
            if row < 0 or col < 0:
                return 0
            
            
            return dp(row, col - 1) + dp(row - 1, col)
        
        
        return dp(m - 1, n - 1)
