class Solution:
    def fib(self, n: int) -> int:
        temp = [0]*(n+1)
        if n ==0:
            return 0
        if n == 1:
            return 1
        else:
            temp[0], temp[1] = 0,1
            for i in range(2,n+1):
                temp[i] = temp[i-1] + temp[i-2]
            return temp[-1]
        