from functools import cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        max_num = (10001 * 367)

        @cache
        def dp(index):
            if index >= len(days):
                return 0           
            oneDayCost = costs[0] + dp(index + 1)            
            next7Index = index
            while next7Index < len(days) and days[next7Index] < days[index] + 7:
                next7Index += 1
            sevenDayCost = costs[1] + dp(next7Index)            
            next30Index = index
            while next30Index < len(days) and days[next30Index] < days[index] + 30:
                next30Index += 1
            thirtyDayCost = costs[2] + dp(next30Index)            
            return min(oneDayCost, sevenDayCost, thirtyDayCost)

        return dp(0)
