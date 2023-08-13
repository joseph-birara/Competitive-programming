class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n <2:
            return n
        if n == 2:
            return 1
        if n== 3:
            return 2
        
        else:
            first = 0
            second = 1
            third = 1
            result = 0
            for i in range(3,n):
                result = first + second + third
                first = second 
                second = third
                third = result 
            return first + second + third 
            
        
        