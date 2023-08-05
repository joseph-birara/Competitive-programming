class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [[0] * (amount + 1) for _ in range(len(coins))]

        for i in range(len(coins)):
            dp[i][0] = 1

        for i in range(1, amount + 1):
            for index, coin in enumerate(coins):
                if coin <= i:
                    dp[index][i] = dp[index - 1][i] + dp[index][i - coin]
                else:
                    dp[index][i] = dp[index - 1][i]

        return dp[len(coins) - 1][amount]
