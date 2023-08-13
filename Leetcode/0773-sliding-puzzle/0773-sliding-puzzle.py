class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
   
        target = [[1, 2, 3], [4, 5, 0]]  # Target state
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # 4-directional movements

        rows, cols = len(board), len(board[0])
        queue = deque([board])  # Start from initial board configuration
        visited = set()
        visited.add(tuple(tuple(row) for row in board))
        moves = 0

        while queue:
            moves += 1
            size = len(queue)
            for _ in range(size):
                curr_board = queue.popleft()
                if curr_board == target:
                    return moves - 1

                # Find the position of the empty square (0)
                for i in range(rows):
                    for j in range(cols):
                        if curr_board[i][j] == 0:
                            empty_row, empty_col = i, j

                # Try moving the empty square in all 4 directions
                for drow, dcol in directions:
                    new_row, new_col = empty_row + drow, empty_col + dcol
                    if 0 <= new_row < rows and 0 <= new_col < cols:
                        new_board = [row[:] for row in curr_board]
                        new_board[empty_row][empty_col], new_board[new_row][new_col] = new_board[new_row][new_col], new_board[empty_row][empty_col]
                        new_board_tuple = tuple(tuple(row) for row in new_board)
                        if new_board_tuple not in visited:
                            visited.add(new_board_tuple)
                            queue.append(new_board)

        return -1  # Target state cannot be reached

    #

        