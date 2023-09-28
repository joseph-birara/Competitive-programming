class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n = len(word1)
        m = len(word2)

        dp = [["inf"]*(m+1) for i in range(n+1)]

        for i in range(m+1):
            dp[n][i] = m-i
        for i in range(n+1):
            dp[i][m] = n-i
        
        for i in range(n-1, -1, -1):
            for j in range(m-1,-1,-1):
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i+1][j+1]
                else:
                    dp[i][j] =  1+ min(dp[i+1][j+1], dp[i][j+1], dp[i+1][j])
        
       
        return dp[0][0]