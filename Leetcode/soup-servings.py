class Solution:
    def soupServings(self, N: int) -> float:   
        if N == 0:
            return 0.5    
      
        if N >= 5000:
            return 1.0  

        N = (N + 24) // 25  

        if N <= 1:
            return 0.625

        dp = [[0] * (N + 1) for _ in range(N + 1)]
        dp[0][0] = 0.5

        for i in range(1, N + 1):
            dp[i][0] = 0.0

        for j in range(1, N + 1):
            dp[0][j] = 1.0

        for i in range(1, N + 1):
            for j in range(1, N + 1):
                dp[i][j] = 0.25 * (dp[max(i - 4, 0)][j] + dp[max(i - 3, 0)][max(j - 1, 0)] +
                                  dp[max(i - 2, 0)][max(j - 2, 0)] + dp[i - 1][max(j - 3, 0)])

        return dp[N][N]








        