class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        
        """
        nums = nums1.copy()
        x =0
        y=0
        k=0
        while x<m and y<n:
            if nums[x]<nums2[y]:
                nums1[k]=nums[x]
                x+=1
            else :
                nums1[k]=nums2[y]
                y+=1
            k +=1
        while x<m:
            nums1[k]=nums[x]
            k+=1
            x+=1
        while y<n:
            
            nums1[k]=nums2[y]
            k+=1
            y+=1
        
      
        
        
        
        