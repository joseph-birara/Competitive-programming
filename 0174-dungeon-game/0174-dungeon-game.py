class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
       
        if not dungeon:
            return 0

        m, n = len(dungeon), len(dungeon[0])
        dp = [[0] * n for _ in range(m)]

        # Initialize the bottom-right corner.
        dp[m - 1][n - 1] = max(1, 1 - dungeon[m - 1][n - 1])

        # Fill in the last column and last row.
        for i in range(m - 2, -1, -1):
            dp[i][n - 1] = max(dp[i + 1][n - 1] - dungeon[i][n - 1], 1)
        for j in range(n - 2, -1, -1):
            dp[m - 1][j] = max(dp[m - 1][j + 1] - dungeon[m - 1][j], 1)

        # Fill in the rest of the table.
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_next = min(dp[i + 1][j], dp[i][j + 1])
                dp[i][j] = max(min_next - dungeon[i][j], 1)

        return dp[0][0]




        