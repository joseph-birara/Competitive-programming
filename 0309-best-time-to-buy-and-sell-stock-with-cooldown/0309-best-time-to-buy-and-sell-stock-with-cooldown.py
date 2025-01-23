class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Initialize states for day 0
        hold = -prices[0]
        sell = 0
        rest = 0
        
        for i in range(1, len(prices)):
            prev_hold, prev_sell, prev_rest = hold, sell, rest
            
            # Update states for day i
            hold = max(prev_hold, prev_rest - prices[i])
            sell = prev_hold + prices[i]
            rest = max(prev_rest, prev_sell)
        
        # The result will be the max of `sell` or `rest`
        return max(sell, rest)
