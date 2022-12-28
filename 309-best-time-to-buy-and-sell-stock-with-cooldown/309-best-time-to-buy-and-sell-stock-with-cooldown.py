class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # State: Buying or Selling?
        # If Buy -> i + 1
        # If Sell -> i + 2

        temp = {}  # key=(i, buying) val=max_profit

        def func(i, buying):
            if i >= len(prices):
                return 0
            if (i, buying) in temp:
                return temp[(i, buying)]

            cool = func(i + 1, buying)
            if buying:
                buy = func(i + 1, not buying) - prices[i]
                temp[(i, buying)] = max(buy, cool)
            else:
                sell = func(i + 2, not buying) + prices[i]
                temp[(i, buying)] = max(sell, cool)
            return temp[(i, buying)]

        return func(0, True)