class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        text1 = s
        text2 = s[::-1]
        n = len(text1) +1
        m = len(text2)+1
        dp = [[0]*m for j in range(n)]
        for i in range(n-2, -1,-1):
            for j in range(m-2, -1,-1):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else :
                    dp[i][j] = max(dp[i+1][j], dp[i][j+1])
        return dp[0][0]
        