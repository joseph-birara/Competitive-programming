class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
               
        n = len(nums)
        min_num = float('inf')
        mid_num = float('inf')

        for num in nums:
            if num <= min_num:
                min_num = num
            elif num <= mid_num:
                mid_num = num
            else:
                return True

        return False
        
        