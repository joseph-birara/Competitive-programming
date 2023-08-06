class Solution:
    def maximumBags(self, capacity: List[int], rocks: List[int], additionalRocks: int) -> int:
        
        diff = [capacity[i]- rocks[i] for i in range(len(capacity))]
        
        diff.sort()
        print(diff)
        
        for i in range(len(diff)):
            if diff[i] and additionalRocks>=  diff[i]:
                
                additionalRocks -= diff[i]
                diff[i] = 0
               
                
       
                
        return diff.count(0)
                    
                
        