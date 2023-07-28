class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        
        five = 0
        ten = 0
        for num in bills :
            if num == 5:
                five +=1
            elif num == 10:
                if not five :
                    return False
                else:
                    five -=1
                    ten +=1
            else:
                if five and ten:
                    five -= 1
                    ten -=1
                elif five >=3:
                    five -=3
                else:
                    return False
       
        return True
            
            
            
        
        
        