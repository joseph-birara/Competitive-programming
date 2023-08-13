class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        
        costs.sort(key=lambda x: x[0] - x[1])
        minCost = 0

        n = len(costs) // 2
        for i in range(n):
            minCost += costs[i][0]  # Fly the person to city a

        for i in range(n, 2 * n):
            minCost += costs[i][1]  # Fly the person to city b

        return minCost
