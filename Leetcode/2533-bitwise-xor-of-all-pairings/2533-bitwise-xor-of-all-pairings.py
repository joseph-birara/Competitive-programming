class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        num1 = 0
        num2 = 0

        n,m = len (nums1), len(nums2)

        for num in nums1:
            if m % 2 == 1:
                num1  ^= num        
        for num in nums2:
            if n % 2 == 1:
                num2 ^= num
        
        return num1 ^ num2


        
        