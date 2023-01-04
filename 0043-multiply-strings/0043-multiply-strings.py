class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        d = {"0":0,"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9}
        num1 = num1[::-1]
        num2= num2[::-1]
        expo1, expo2 = 0, 0
        temp1, temp2 = 0,0
        
        for character in num1:
            temp1 += d[character]* (10**expo1)
            expo1 +=1
        
        for character in num2:
            temp2 += d[character]* (10**expo2)
            expo2 +=1
        return str(temp1*temp2)
            
            
            
        