class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        result =0
        for index in range(len(strs[0])):
            c = strs[0][index]
            for word in strs[1:]:
               
                
                if c> word[index] :
                    
                    result+=1
                    break
                else:
                    c = word[index]
        return result 
                    
            
        
        