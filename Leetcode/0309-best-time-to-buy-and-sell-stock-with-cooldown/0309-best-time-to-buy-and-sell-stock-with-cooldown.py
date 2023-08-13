class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n <= 1:
            return 0

        buy = [-prices[0]] + [0] * (n - 1)
        sell = [0] * n
        cooldown = [0] * n

        for i in range(1, n):
            buy[i] = max(cooldown[i - 1] - prices[i], buy[i - 1])
            sell[i] = max(buy[i - 1] + prices[i], sell[i - 1])
            cooldown[i] = max(sell[i - 1], cooldown[i - 1])

        return max(sell[n - 1], cooldown[n - 1])
