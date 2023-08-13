class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        
        def inBound(row,col):
            return 0<= row < n and 0<= col < n
        
        
        drxn = [[0,1],[0,-1],[1,0],[-1,0]]
        landOne = deque()
        q = deque()        
        n = len(grid)
        visited = set()
        
        
        # get the first land
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
                    landOne.append((i,j))
                    visited.add((i,j))
                    break
            if len(q) == 1:
                break
        # add all cells of land one
        
        while q :
            
            size = len(q)            
            for i in range(size):
                row, col = q.popleft()
                for x, y in drxn:
                    new_row = row + x
                    new_col = col +y 
                    
                    if inBound(new_row,new_col) and (new_row,new_col) not in visited and grid[new_row][new_col] ==1 :
                        visited.add((new_row,new_col))
                        q.append((new_row,new_col))
                        landOne.append((new_row,new_col))
        
        moves = 0
        while landOne:            
            
            size = len(landOne)            
            for i in range(size):
                row, col = landOne.popleft()
                for x, y in drxn:
                    new_row = row + x
                    new_col = col +y 
                    
                    if inBound(new_row,new_col) and (new_row,new_col) not in visited :
                        if grid[new_row][new_col] ==1 :
                            return moves
                        visited.add((new_row,new_col))                       
                        landOne.append((new_row,new_col))
            moves += 1
        return -1
            
        
                        
                        
                
        