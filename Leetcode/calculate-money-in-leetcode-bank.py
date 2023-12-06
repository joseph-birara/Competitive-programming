class Solution:
    def totalMoney(self, remaining_days: int) -> int:
        result = 0
        start_value = 1

        while remaining_days > 0:
            for day_increment in range(min(remaining_days, 7)):
                result += start_value + day_increment

            remaining_days -= 7
            start_value += 1

        return result
