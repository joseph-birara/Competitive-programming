class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        temp = ''
        n = len(nums)
        for i in range(n):
            large = nums[i]
            for j in range(i+1,n):
                
                if int(str(large) + str(nums[j]) )< int(str(nums[j]) + str(large)):
                    
                    large = nums[j]
                    nums[j], nums[i] = nums[i], nums[j]
                    
            
        for i in nums:
            temp += str(i) 
            
        if temp[0] == '0':
            return temp[0]
        return temp
                
            
        
            
        
        