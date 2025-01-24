class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]


        visited = [[0 for i in range(len(grid[0]))] for j in range(len(grid))]

        ans = [0]

        def inbound(row, col):
            return (0 <= row < len(grid) and 0 <= col < len(grid[0]))

            
        def dfs(row, col):
            # base case
            visited[row][col] = True
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if grid[row][col] == 1:
                        
                    if not inbound(new_row, new_col) or grid[new_row][new_col] == 0:
                        ans[0] += 1
                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    dfs(new_row, new_col)
        dfs(0,0)

        return ans[0]