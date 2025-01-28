class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:


        
        m, n = len(grid), len(grid[0])
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            # If out of bounds or land cell, stop the DFS
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == 0:
                return 0

            # Collect the fish at the current cell and mark it visited (set to 0)
            fish = grid[r][c]
            grid[r][c] = 0

            # Explore all adjacent cells
            for dr, dc in directions:
                fish += dfs(r + dr, c + dc)
            
            return fish

        max_fish = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:  # Start from each water cell
                    max_fish = max(max_fish, dfs(r, c))

        return max_fish
