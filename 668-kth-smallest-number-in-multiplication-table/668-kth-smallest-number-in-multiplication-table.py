class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        
        l = 1
        r = m*n
        ans = r
        while(l<=r):
            mid = (l+r)//2
            cnt = 0;
            for i in range(1,m+1):
                cnt += min(n,mid//i)
            
            if(cnt>=k):
                ans = mid
                r = mid - 1
            
            else:
                l = mid + 1
            
        
        return ans
                
        
            
        