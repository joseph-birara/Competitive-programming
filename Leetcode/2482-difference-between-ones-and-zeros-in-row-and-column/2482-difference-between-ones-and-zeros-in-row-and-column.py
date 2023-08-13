class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        grid_length =len(grid)
        grid_width = len(grid[0])
        
        result_grid = [[0] * grid_width for _ in range(grid_length)]
        
        # count number of ones in a row and column
        onesRow = [row.count(1) for row in grid]
        onesCol = [col.count(1) for col in zip(*grid)]
        
        for index in range(grid_length):
            
            for inerIndex in range(grid_width):
                # zeros in row and column
                zerosRow =  grid_width- onesRow[index]
                zerosCol = grid_length - onesCol[inerIndex]
                total = zerosRow + zerosCol
                
                result_grid[index][inerIndex] = onesRow[index] + onesCol[inerIndex] -total
        return result_grid
        
        
        