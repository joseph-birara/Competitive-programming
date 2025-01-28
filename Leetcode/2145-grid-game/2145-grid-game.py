class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        firstSum = sum(grid[0])
        secondSum = 0
        res = float('inf')
        n = len(grid[0])

        for i in range(n):
            firstSum -= grid[0][i]
            res = min(res, max(firstSum, secondSum))
            secondSum += grid[1][i]
        return res


        


        