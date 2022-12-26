class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        sum = 0
        n = len(piles)
        
        
        for i in range(int(n/3),n , 2):
            sum += piles[i]
        return sum