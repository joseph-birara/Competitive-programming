class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        less_than_pivot =[]
        greaterThan_pivot =[]
        equal_to_pivot =[]
        arranged_nums = []
        
        for element in nums:
            if element > pivot:
                greaterThan_pivot.append(element)
            elif element < pivot :
                less_than_pivot.append(element)
            else:
                equal_to_pivot.append(element)
        for element in less_than_pivot:
            arranged_nums.append(element)
            
                
        for element in  equal_to_pivot:
            arranged_nums.append(element)
        for element in  greaterThan_pivot:
            arranged_nums.append(element)
        return arranged_nums
                
        
        
        