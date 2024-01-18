class Solution:
    def climbStairs(self, n: int) -> int:
        if n<= 1:
            return n

        ways = [1,2]

        for i in range(2,n):           
            ways.append(ways[-2] + ways[-1])  
             
        return  ways[-1]

        