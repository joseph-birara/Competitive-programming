class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows,cols = len(grid),len(grid[0])
        temp = 0
        def dfsFunction(r,c):
            drxn = [[0,1],[0,-1],[1,0],[-1,0]]
            if 0 <= r < rows and  0<=c<cols and grid[r][c] == 1:
                grid[r][c] = -1
                for i,j in drxn:
                    dfsFunction(r + i,c + j)
        for i in range(cols):
            for j in [0,rows - 1 ]:
                dfsFunction(j,i)
        
        for i in range(rows):
            for j in [0, cols - 1]:
                dfsFunction(i,j)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    temp += 1
        return temp