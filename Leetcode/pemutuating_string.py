class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = Counter(s1)
        m = len(s1)
        n = len(s2)
        left = 0
        d = Counter('')
        
        for i in range(n):
            
            if (i - left)+1 == m:
                d = Counter(s2[left:i+1])
                if d == count:
                    return True
                else:
                    d[s2[left]] -=1
                    left +=1
                    
        return False
        
        
