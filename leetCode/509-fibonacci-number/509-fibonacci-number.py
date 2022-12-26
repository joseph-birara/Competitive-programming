class Solution:
    def fib(self, n: int) -> int:
        temp = [0,1]
        if n == 0:
            return 0
        
        for i in range(2,n+1):
            temp.append(temp[i-1] + temp[i-2]) 
        return temp[-1]
        