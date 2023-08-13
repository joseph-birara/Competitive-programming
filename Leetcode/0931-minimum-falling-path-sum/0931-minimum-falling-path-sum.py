class Solution:
    def minFallingPathSum(self,matrix):
        n = len(matrix)
        dp = [[0] * n for _ in range(n)]

        # Copy values from the first row to the auxiliary matrix
        for col in range(n):
            dp[0][col] = matrix[0][col]

        # Iterate through the remaining rows
        for row in range(1, n):
            for col in range(n):
                # Calculate the minimum sum for each position
                if col == 0:
                    dp[row][col] = matrix[row][col] + min(dp[row - 1][col], dp[row - 1][col + 1])
                elif col == n - 1:
                    dp[row][col] = matrix[row][col] + min(dp[row - 1][col], dp[row - 1][col - 1])
                else:
                    dp[row][col] = matrix[row][col] + min(dp[row - 1][col - 1], dp[row - 1][col], dp[row - 1][col + 1])

        # Find the minimum sum in the last row
        min_sum = min(dp[n - 1])

        return min_sum

        