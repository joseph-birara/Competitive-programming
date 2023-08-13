class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0] *( n+1)        
        
        for i in range(1,n+1):            
            if i == 1:
                arr[1] = 1
                
            if 2 <= (2 * i) <= n:
                arr[i*2] = arr[i]
            if 2 <= (2 * i) + 1 <= n:
                
                arr[(2 * i) + 1]  = arr[i] + arr[i+1]
        
        return max(arr)
            
            
            
            
            
                
        
        