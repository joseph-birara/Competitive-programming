class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        
        combined = list(zip(growTime, plantTime))
        combined.sort(reverse =True, key = lambda x: x[0])
        ans= 0
        temp = 0
        
        for grow , plant in combined:
            
            temp += plant
            ans = max(ans, temp+grow)
            
        return ans
            
            
        
        
        
        
        
        