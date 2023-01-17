class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
              
         
        length = len(names)
        
        for index in range (1,length):
            j = index
            while j >0 and heights[j] >heights[j-1]:
                heights[j], heights[j-1] = heights[j-1],heights[j]
                names[j], names[j-1] = names[j-1],names[j]
                j -=1
            
        
        return names
        
                
                
        