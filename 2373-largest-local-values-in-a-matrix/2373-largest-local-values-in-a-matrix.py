class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        length = len(grid)
        result  = [[0]* (length-2) for _ in range(length-2)]
        for row in range(len(grid)-2):
            for column in range(len(grid[0])-2):
                 result [row][column] = max(
                    grid[row][column], grid[row][column + 1], grid[row][column + 2],
                    grid[row + 1][column], grid[row + 1][column + 1], grid[row + 1][column + 2],
                    grid[row + 2][column], grid[row + 2][column + 1], grid[row + 2][column + 2]
                )
        
                
        
        return result 