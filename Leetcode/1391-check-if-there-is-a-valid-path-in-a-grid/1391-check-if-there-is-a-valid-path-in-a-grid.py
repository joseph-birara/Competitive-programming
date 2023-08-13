class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        
        # Define the possible directions for each type of street
        directions = {
            1: [(0, 1), (0, -1)],
            2: [(1, 0), (-1, 0)],
            3: [(1, 0), (0, -1)],
            4: [(1, 0), (0, 1)],
            5: [(-1, 0), (0, -1)],
            6: [(-1, 0), (0, 1)]
        }
        
        # Define a function to check if a given move is valid
        def isValidMove(row: int, col: int, move: Tuple[int, int]) -> bool:
            new_row, new_col = row + move[0], col + move[1]
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                return False
            next_street = grid[new_row][new_col]
            if (-move[0], -move[1]) not in directions[next_street]:
                return False
            return True
        
        # Define the DFS function to explore all possible paths
        def dfs(row: int, col: int, visited: set) -> bool:
            if (row, col) == (len(grid)-1, len(grid[0])-1):
                return True
            visited.add((row, col))
            for move in directions[grid[row][col]]:
                if isValidMove(row, col, move):
                    new_row, new_col = row + move[0], col + move[1]
                    if (new_row, new_col) not in visited:
                        if dfs(new_row, new_col, visited):
                            return True
            return False
        
        # Start the DFS from the upper-left cell
        return dfs(0, 0, set())
