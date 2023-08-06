class Solution:
    def rob(self, nums: List[int]) -> int: 
        
        if len(nums)<2:
            return nums[0]
        r1,r2 = 0,0
        for money in nums[1:]:
            temp = max(r1+money, r2)
            r1 = r2
            r2= temp
            
        one, two = 0 , 0        
        for num in nums[:len(nums)-1]:
            temp = max(one + num, two)
            one = two
            two = temp
        return max(two, r2)
        
        