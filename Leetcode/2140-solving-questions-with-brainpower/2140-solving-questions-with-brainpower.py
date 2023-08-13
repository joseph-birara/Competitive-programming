class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)

        for i in range(n - 1, -1, -1):
            p, bp = questions[i]

            next_q = i + bp + 1
            next_q = n if next_q >= n else next_q

            dp[i] = max(dp[i+1], p + dp[next_q])

        return dp[0]
