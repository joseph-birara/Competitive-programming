class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        memo = defaultdict(int)    
        
        for num in arr:            
            memo[num] =memo[num-difference] +1
            
        return max(memo.values())
            
        
            
        