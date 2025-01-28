class Solution:
    def tribonacci(self, n: int) -> int:
        if n <2:
            return n
        if n == 2:
            return 1
        
        zero = 0
        two = one = 1

        for i in range(3,n+1):
            three = one + two + zero
            zero = one
            one = two
            two = three
        return three
        