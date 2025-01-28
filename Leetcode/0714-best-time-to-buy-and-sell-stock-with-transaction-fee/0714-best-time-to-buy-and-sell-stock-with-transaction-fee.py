class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        


        preS = 0
        preB = -prices[0]

        for i in range(len(prices)):
            preB = max(preB,preS - prices[i])
            preS = max(preS, preB + prices[i] - fee)

        return preS

        