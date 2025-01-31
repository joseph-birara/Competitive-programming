class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        


        n = len(grid)
        island_id = 2  # Start labeling from 2
        island_sizes = {0: 0}  # Map island_id -> size

        # DFS to label islands and compute sizes
        def dfs(r, c, id):
            if r < 0 or c < 0 or r >= n or c >= n or grid[r][c] != 1:
                return 0
            grid[r][c] = id  # Mark the cell with its island ID
            return 1 + dfs(r+1, c, id) + dfs(r-1, c, id) + dfs(r, c+1, id) + dfs(r, c-1, id)

        # Step 1: Label all islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    island_sizes[island_id] = dfs(r, c, island_id)
                    island_id += 1

        # Step 2: Check for potential largest island by flipping a 0
        max_island = max(island_sizes.values(), default=0)  # Max existing island size
        
        directions = [(0,1), (1,0), (0,-1), (-1,0)]  # Right, Down, Left, Up

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen = set()
                    new_size = 1  # Start with size 1 (flipping this 0)
                    
                    # Check all 4 neighbors
                    for dr, dc in directions:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] > 1:
                            seen.add(grid[nr][nc])
                    
                    # Sum up unique island sizes
                    new_size += sum(island_sizes[i] for i in seen)
                    max_island = max(max_island, new_size)

        return max_island
