class Solution:
    def countOrders(self, n: int) -> int:
        res = (factorial(2*n)//(pow(2,n))) % (10**9 +7)

        return res
        
