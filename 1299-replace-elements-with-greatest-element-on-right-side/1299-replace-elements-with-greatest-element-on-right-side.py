class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        
        length = len(arr)
        
        max_ele = arr[-1]
        for index in range(length-2,-1,-1):
            curr = arr[index]
            arr[index] = max_ele
            if curr > max_ele:
                max_ele = curr
        arr[-1] = -1
          
        return arr
            
        