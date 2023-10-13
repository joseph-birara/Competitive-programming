class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        rvsed = num[::-1]
        
        left = 0
        while left<len(num) and rvsed[left] == "0":
                left +=1
        return num[:len(num)-left]
        