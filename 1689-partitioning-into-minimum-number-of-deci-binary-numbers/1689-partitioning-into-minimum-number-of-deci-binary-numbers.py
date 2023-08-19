class Solution:
    def minPartitions(self, n: str) -> int:
        ans = 0
        
        for num in str(n):
            ans = max(ans, int(num))
        return ans
        