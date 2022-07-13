class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        temp = []
         
        n = len(nums1)
        k = len(nums2)
        for i in nums1:
            for j in range(k):
                if i == nums2[j]:
                    flag = False
                    
                    for item in nums2[j:]:
                        if item > i:
                            temp.append(item)
                            flag = True
                            break
                    if  not flag:
                        temp.append(-1)
                    break
        return temp
                            
                    
                    
        