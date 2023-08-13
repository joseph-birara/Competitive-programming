class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        
        if numOnes +numZeros  >= k:
            return min(numOnes, k)
        else :
            t = k - (numOnes +numZeros)
            return numOnes  - t
            
        
        
        
        