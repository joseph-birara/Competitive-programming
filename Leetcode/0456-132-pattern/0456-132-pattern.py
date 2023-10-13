class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        
        middle = -math.inf
        stack = []
        
        for i in range(n-1,-1,-1):
            if nums[i] < middle:
                return True
            while stack and stack[-1] < nums[i]:
                middle = stack.pop()
            stack.append(nums[i])
        return False
            
            
        
        