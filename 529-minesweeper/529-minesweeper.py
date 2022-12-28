class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        cr,cc = click[0],click[1]
        visited = set()
        if board[cr][cc] == "M":
            board[cr][cc] = "X"
            return board
        ro,co = len(board),len(board[0])
        def dfsFunction(r,c):
            if r == ro or r < 0 or c == co or c < 0 or (r,c) in visited:
                return
            visited.add((r,c))
            if board[r][c] == "M":
                return
            
            mines = 0
            dirn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
            for i,j in dirn:
                nr,nc = i + r, j + c
                if 0 <= nr < ro and 0 <= nc < co and board[nr][nc] == 'M' :
                    mines += 1
            if mines > 0:
                board[r][c] = str(mines)
                return
            else:
                board[r][c] = "B"
            for i,j in dirn:
                nr,nc = i + r, j + c
                dfsFunction(nr,nc)
        dfsFunction(cr,cc)
        return board