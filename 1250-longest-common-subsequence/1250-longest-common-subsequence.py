class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        common = [[0] * (m + 1) for _ in range(n + 1)]

        for j in range(1, n + 1):
            for i in range(1, m + 1):
                if text1[j - 1] == text2[i - 1]:
                    common[j][i] = common[j - 1][i - 1] + 1
                else:
                    common[j][i] = max(common[j - 1][i], common[j][i - 1])

        return common[n][m]
