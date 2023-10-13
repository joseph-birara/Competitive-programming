class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n == 1:
            return 0
        
        current_jump_end = 0  
        next_jump_end = 0    
        jumps = 0             
        
        for i in range(n - 1):
            next_jump_end = max(next_jump_end, i + nums[i])             
            if i == current_jump_end:
                jumps += 1
                current_jump_end = next_jump_end  
            
            if current_jump_end >= n - 1:
                break
        
        return jumps
