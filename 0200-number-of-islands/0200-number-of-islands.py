class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        dxn = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(grid), len(grid[0])

        def isValid(row, col):
            inBound = 0 <= row < n and 0 <= col < m  
            one = inBound and grid[row][col] == '1'  
            notVisited = (row, col) not in visited  
            return one and notVisited

        def dfs(row, col):
            visited.add((row, col))  
            for x, y in dxn:  
                new_row, new_col = row + x, col + y
                if isValid(new_row, new_col):
                    dfs(new_row, new_col)

        visited = set()
        ans = 0  
        
        for i in range(n):
            for j in range(m):
                if isValid(i, j): 
                    dfs(i, j)  
                    ans += 1  

        return ans
