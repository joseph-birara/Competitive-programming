class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        
        result = abs(dividend)//abs(divisor)
        if dividend * divisor <0:
            result = -(result)
        
        
        minus_limit = -(2**31)
        plus_limit = (2**31 - 1)
        result = min(max(result, minus_limit), plus_limit)
        return result
        