class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        temp = num-3
          
        
        if temp% 3 == 0:
            firstNum = temp//3
            return [firstNum,firstNum +1,firstNum+2]
        else:
            return []
            
        