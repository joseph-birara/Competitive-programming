class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        visited = set((0,0))

        dirxns = [(0,1),(0,-1),(1,0),(1,-1),(1,1),(-1,0),(-1,-1),(-1,1)]

        q = deque([(0,0,1)])

        row_len = len(grid)
        

        while q :
            row , col, distance = q.popleft()

            if (min(row,col) <0 or max(row,col)>=row_len  or grid[row][col] == 1):
                continue

            if row == row_len -1 and col == row_len -1 :
                return distance 
            
            for x, y in dirxns:
                if (row+x, y + col) not in visited:
                    q.append((row+x, y + col, distance+1))
                    visited.add((row+x, y + col))
            
        return -1