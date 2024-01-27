class Solution:
    def kInversePairs(self, n: int, k: int) -> int:
        MOD = 10**9 + 7

        # Initialize a 2D array for dynamic programming
        dp = [[0] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 1

        # Calculate the number of arrays with k inverse pairs using dynamic programming
        for i in range(1, n + 1):
            prefix_sum = 0
            for j in range(k + 1):
                prefix_sum = (prefix_sum + dp[i-1][j]) % MOD

                if j >= i:
                    prefix_sum = (prefix_sum - dp[i-1][j-i]) % MOD

                dp[i][j] = prefix_sum

        return dp[n][k]