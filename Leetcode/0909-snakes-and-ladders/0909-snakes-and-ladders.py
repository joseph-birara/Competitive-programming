class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        
       

        n = len(board)
        destination = n * n
        queue = deque([1])  # Start from square 1
        visited = [False] * (n * n + 1)  # visited array
        visited[1] = True
        moves = 0

        while queue:
            moves += 1
            size = len(queue)
            for _ in range(size):
                curr = queue.popleft()
                for i in range(1, 7):
                    next_square = curr + i
                    if next_square > n * n:
                        break

                    # Calculate row and column indices of the next square
                    row = n - 1 - (next_square - 1) // n
                    col = (next_square - 1) % n

                    if row % 2 == n % 2:
                        col = n - 1 - col  # Adjust column index for Boustrophedon pattern

                    if board[row][col] != -1:  # Check for snake or ladder
                        next_square = board[row][col]

                    if not visited[next_square]:
                        visited[next_square] = True
                        queue.append(next_square)

                        if next_square == destination:
                            return moves

        return -1  # Destination square cannot be reached



            
            
        
        
        