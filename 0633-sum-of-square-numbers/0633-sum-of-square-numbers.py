class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        max_ = math.sqrt(c)
        max_ = math.ceil(max_)
        
        min_ = 0
        while min_ <= max_:
            num = min_*min_ + max_*max_
            if num == c:
                return True
            if num > c:
                max_ -=1
            if num < c:
                min_ +=1
        return False
            
        