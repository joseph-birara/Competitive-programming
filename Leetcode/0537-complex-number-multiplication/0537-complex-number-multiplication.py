class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        result_complex = ''
        
        split_num1 = list(num1.split("+"))
        
        split_num1[1] = split_num1[1][:len(split_num1[1])-1]
        
        split_num2 = list(num2.split("+"))
        
        
        split_num2[1] = split_num2[1][:len(split_num2[1])-1]
       
        
        real_part = int(split_num1[0]) * int(split_num2[0]) + -1* int(split_num1[1]) * int(split_num2[1])
        imagnary_part = int(split_num1[1]) * int(split_num2[0]) +  int(split_num1[0]) * int(split_num2[1])
        
        
        result_complex += str(real_part) + "+" +str(imagnary_part)+"i"
        return result_complex