class Solution:
    def dp(self, x, y, n, visited, k):
        if k < 0:
            return 1
        if x < 0 or x >= n or y < 0 or y >= n:
            return 0
        if (x, y, k) in visited:
            return visited[(x, y, k)]

        # Initialize the probability for the current position (x, y)
        probability = 0

        # Define all possible moves of the knight
        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]

        # Calculate the probability for each move and add it to the overall probability
        for move in moves:
            probability += self.dp(x + move[0], y + move[1], n, visited, k - 1) * 1 / 8

        # Memoize the result and return the probability
        visited[(x, y, k)] = probability
        return probability

    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        return self.dp(row, column, n, {}, k)
