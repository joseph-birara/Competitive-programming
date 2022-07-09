class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
    
        hash = defaultdict(int)
        var = 0 
        
        for i in nums:
            target = k - i
            
            if hash[target] > 0:
                hash[target] -= 1
                var += 1
            else:
                hash[i] += 1
                
        return var
        