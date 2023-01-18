testCases = int (input())
res = []
for _ in range(testCases):
    
    grid_size = int (input())
    grid = []
    operation_count= 0

    for k in range(grid_size):
        
        grid.append(input())
   

    for row_index in range(grid_size):
        temp =[]
        for col_index in range(grid_size):
            temp.append(grid[row_index][col_index])
            temp.append(grid[col_index][-1-row_index])
            temp.append(grid[-1-row_index][-1-col_index])
            temp.append(grid[-1-col_index][row_index])

            
    # 
    res.append(operation_count//2)
print(res)





