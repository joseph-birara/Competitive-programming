class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:        
        for row in pieces:
            
            if row[0] not in arr:
                return False
        
            pre = arr.index(row[0])
            for num in row[1:]:
                if num not in arr:
                    return False
                temp = arr.index(num)
                if pre >temp:
                    return False
                if pre + 1 !=temp:
                    return False
                pre = temp
        return True
                
                
                
        
        
        