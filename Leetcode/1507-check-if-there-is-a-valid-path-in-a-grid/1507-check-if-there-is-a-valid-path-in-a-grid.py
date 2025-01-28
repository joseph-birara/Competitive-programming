class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        
        directions = {
            1: [(0, 1), (0, -1)],    
            2: [(1, 0), (-1, 0)],     
            3: [(1, 0), (0, -1)],     
            4: [(1, 0), (0, 1)],      
            5: [(-1, 0), (0, -1)],    
            6: [(-1, 0), (0, 1)]      
        }
        
        # Function to check if a move is valid (within grid bounds and respecting street types)
        def isValidMove(row, col, move):
            # Calculate new row and column after the move
            new_row, new_col = row + move[0], col + move[1]
            
            # Check if the new position is within bounds of the grid
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                return False
            
            # Get the type of street at the new position
            next_street = grid[new_row][new_col]
            
            # Check if the opposite direction of the move is valid for the next street
            if (-move[0], -move[1]) not in directions[next_street]:
                return False
            
            return True
        
        # Depth-first search function to explore possible paths from current position
        def dfs(row: int, col: int, visited: set) -> bool:
            # Base case: if we've reached the bottom-right corner, return True
            if (row, col) == (len(grid) - 1, len(grid[0]) - 1):
                return True
            
            # Mark the current cell as visited
            visited.add((row, col))
            
            # Explore all valid moves from the current position
            for move in directions[grid[row][col]]:
                if isValidMove(row, col, move):
                    new_row, new_col = row + move[0], col + move[1]
                    if (new_row, new_col) not in visited:
                        # Recursively explore the new position
                        if dfs(new_row, new_col, visited):
                            return True
            return False
        
        # Start DFS from the top-left corner (0, 0)
        visited = set()
        return dfs(0, 0, visited)
