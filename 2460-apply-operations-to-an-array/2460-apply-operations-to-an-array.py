class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for index in range(n-1):
            if nums[index] == nums[index+1]:
                nums[index] = nums[index]*2
                nums[index+1] = 0
        result = []
        zeroCount=0
        for element in nums:
            if element !=0:
                result.append(element)
            else:
                zeroCount +=1
        while zeroCount >0:
            result.append(0)
            zeroCount-=1
        
        return result
        
        