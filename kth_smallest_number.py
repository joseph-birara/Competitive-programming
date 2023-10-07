

class Solution:
    def findKthNumber(self,n, k):
        current = 1
        k -= 1          
        while k > 0:          
            steps = 0
            interval_start = current
            interval_end = current + 1
            
            while interval_start <= n:
                steps += min(n + 1, interval_end) - interval_start
                interval_start *= 10
                interval_end *= 10            
            if k >= steps:                
                current += 1
                k -= steps
            else:                
                current *= 10
                k -= 1
        
        return current

            
