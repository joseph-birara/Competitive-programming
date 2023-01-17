class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        
          
         
        length = len(names)  
        
        
        
        for i in range(length):
            
            max_h = heights[i]
            max_index = i
            for j in range(i+1,length):
                if heights[j] > max_h:
                    max_h=heights[j]
                    max_index = j
            heights[i],heights[max_index] = heights[max_index], heights[i]
            names[i],names[max_index] = names[max_index], names[i]
                
        
        return names
                
                
        