class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        
        length = len(arr)
        down , up =0,0
        
        if length <3:
            return False
        for index in range(1,length-1):
            if arr[index-1] <arr[index] >arr[index+1]:
                up +=1
            if arr[index-1] >=arr[index] <=arr[index+1]:
                down +=1
        
            
            
                
       
        return down ==0 and up ==1
                    
                    
        
        
        