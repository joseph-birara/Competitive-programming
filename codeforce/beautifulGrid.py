testCases = int (input())
res = []
# def rotator(grid):
#     row_len = len(grid)
#     col_len = len(grid[0])
#     temp = []
#     for col in zip(*grid):
#         temp.append(col[::-1])
#     return temp

for _ in range(testCases):
    
    grid_size = int (input())
    grid = []
    operation_count= 0

    for k in range(grid_size):
        
        grid.append(input())
   

    for row_index in range(grid_size):
        for col_index in range(grid_size):
            if grid[row_index][col_index] != grid[col_index][row_index]:
               
                operation_count +=1
    # 
    res.append(operation_count//2)
print(res)





