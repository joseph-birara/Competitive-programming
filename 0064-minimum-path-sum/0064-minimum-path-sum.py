class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid) , len(grid[0])
        @cache
        def dp(row,col):
            if row < 0 or col <0 :
                return float('inf')
            if row == col == 0:
                return grid[0][0]
            return grid[row][col] + min(dp(row-1,col), dp(row, col-1))
        
        return dp(n-1,m-1)