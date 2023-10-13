class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:

        stack = [[cost[0]-cost[1],i] for i, cost in enumerate(costs)]
        stack.sort()
        res = 0
        n = len(costs)

        for i in range(n):
            if i <n//2:
                res += costs[stack[i][1]][0]
            else:
                res += costs[stack[i][1]][1]
        return res





        