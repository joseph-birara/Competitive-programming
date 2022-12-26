class Solution:
    def average(self, salary: List[int]) -> float:
        low = salary[0]
        length = len(salary)-2
        res =0
        high = salary[0]
        for money in salary:
            if money >high:
                high = money
            if money < low:
                low = money
            res +=money
            
            
        exclude = low +high
        return (res - exclude)/length
            
            
        