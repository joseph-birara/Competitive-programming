class Solution:
    def maxScore(self, nums: List[int]) -> int:
        
        @cache
        def dfs(nums, k):  
            max_gcd = 0
            
            for i in range(len(nums)):                
                for j in range(i+1, len(nums)):
                    temp = k*gcd(nums[j],nums[i])
                    new_nums = nums[:i] + nums[i+1:j] + nums[j+1:]
                    max_gcd = max(max_gcd, temp 
                    + dfs(new_nums,k+1))
            return max_gcd 
        

        return dfs(tuple(nums),1)
    
                
            
                
        


                

        
