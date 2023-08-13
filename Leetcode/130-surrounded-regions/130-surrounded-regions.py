class Solution:
    def solve(self, board): 
        """
        Do not return anything, modify board in-place instead.
        """
        R, Co = len(board), len(board[0])

        def dfs(r, c):
            if r < 0 or c < 0 or r == R or c == Co or board[r][c] != "O":
                return
            board[r][c] = "T"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        # 1. (DFS) dfs unsurrounded regions (O -> T)
        for r in range(R):
            for c in range(Co):
                if board[r][c] == "O" and (r in [0, R - 1] or c in [0, Co - 1]):
                    dfs(r, c)

        # 2. dfs surrounded regions (O -> X)
        for r in range(R):
            for c in range(Co):
                if board[r][c] == "O":
                    board[r][c] = "X"
                if board[r][c] == "T":
                    board[r][c] = "O"

        
        
        
        
        
        
        
        