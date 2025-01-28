class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        n = len(s)
        if n < k :            
            return False
        hashmap = Counter(s)
        odd = 0
        for key in hashmap :
            if hashmap[key] % 2 == 1:
                odd +=1
        
        return odd <= k


        
        
        