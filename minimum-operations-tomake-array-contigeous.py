class Solution:
    def minOperations(self, nums: List[int]) -> int:

        min_op = n = len(nums)     
        nums = list(set(nums))
        nums.sort()

        for index ,num in enumerate(nums):
            num += (n-1)
            place = bisect_right(nums,num)
            temp = n -(place - index)           
            min_op = min(min_op,temp)
        return min_op





        
