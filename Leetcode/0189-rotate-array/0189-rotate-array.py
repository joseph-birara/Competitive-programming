class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k%len(nums)
        
        for j in range(1,k+1,1):
                      
            nums.insert(0,nums.pop(-1))
        