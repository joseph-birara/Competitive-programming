class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        res = 0
        for item in nums:
            if item !=val:
                nums[res] =item
                res +=1
        
        return res
        