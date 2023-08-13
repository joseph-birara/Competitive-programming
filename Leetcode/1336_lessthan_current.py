class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        l=len(nums)
        temp=[None]*l
       
        for i in range(l):
            
            k=0
            for item in nums:
                if item < nums[i]:
                    k +=1
            temp[i] = k
        return temp
        
