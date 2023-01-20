class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        d = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        
        temp =[]
        n = len(digits)
        if n ==2:          
        
          
            for letter in d[digits[0]]:
                for secod_l in d[digits[1]]:
                    temp.append(letter+secod_l)
                    
        elif n ==1:
            for letter in d[digits[0]]:
                temp.append(letter)
                
        elif n == 3:
             
            for letter in d[digits[0]]:
                for secod_l in d[digits[1]]:
                    for third_l in d[digits[2]]:
                        temp.append(letter+secod_l+third_l)
        elif n == 4:
             
            for letter in d[digits[0]]:
                for secod_l in d[digits[1]]:
                    for third_l in d[digits[2]]:
                        for fourth_l in d[digits[3]]:
                            temp.append(letter+secod_l+third_l+fourth_l)
            
            
        return temp
        
        