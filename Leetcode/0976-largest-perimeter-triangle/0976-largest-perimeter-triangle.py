class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        parameter=0
        nums_length=len(nums)-3
        newNums =sorted(nums)
        
        while nums_length>=0  :
            if newNums[nums_length] +newNums[nums_length+1] >newNums[nums_length+2]:
                parameter = newNums[nums_length] +newNums[nums_length+1] +newNums[nums_length+2]
                break
            else:
                
                nums_length -=1
                
            
        
        return parameter
                    
                    
            
        