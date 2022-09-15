class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rw, cl = len(grid), len(grid[0])
        dp = [[float("inf")]* (cl+1) for d in range(rw+1)]
        dp[rw-1][cl] = 0
        for h in range(rw-1,-1,-1):
            for v in range(cl-1 , -1, -1):
                dp[h][v] = grid[h][v] + min(dp[h+1][v], dp[h][v+1])
        return dp[0][0]
        