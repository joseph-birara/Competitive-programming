class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = 0        
        res = ''      
        for i in range(2,len(num)):
            if num[i] == num[i-1] == num[i-2]:
                res = max(num[i-2:i+1],res)
        return res
            
            
            
        