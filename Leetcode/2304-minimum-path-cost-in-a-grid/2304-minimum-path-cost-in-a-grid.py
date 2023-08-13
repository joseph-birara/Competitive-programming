class Solution:
    def minPathCost(self, grid: List[List[int]], moveCost: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        dp = [[float('inf')] * n for _ in range(m)]

       
        for j in range(n):
            dp[0][j] = grid[0][j]

       
        for i in range(1, m):
            for j in range(n):
                for prev_j in range(n):
                    dp[i][j] = min(dp[i][j], dp[i-1][prev_j] + moveCost[grid[i-1][prev_j]][j] + grid[i][j])
        
        return min(dp[-1])

        