class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        if n == 1:
            return True
        while n !=1:
            n = self.sumSquare(n)
            if n in s and n !=1:
                return False
            if n == 1:
                return True
            
                
            s.add(n)
            print(n)
        
        
            
        
    def sumSquare(self,num):
        sum_ = 0
        while num !=0:
            d = num%10
            sum_ += d*d
            num = num//10
        return sum_
            
        