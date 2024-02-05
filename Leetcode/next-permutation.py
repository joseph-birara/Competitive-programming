class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Step 1: Find the first element to be swapped
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1
        
        # Step 2: If no such element is found, reverse the array
        if i == -1:
            nums.reverse()
            return
        
        # Step 3: Find the smallest element to the right of nums[i] and greater than nums[i]
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        
        # Step 4: Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
        
        # Step 5: Reverse the elements to the right of nums[i]
        nums[i+1:] = reversed(nums[i+1:])