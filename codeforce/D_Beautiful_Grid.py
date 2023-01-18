from collections import Counter, defaultdict


testCases = int (input())
res = []
for _ in range(testCases):
    
    grid_size = int (input())
    grid = []
    operation_count= 0

    for k in range(grid_size):
        
        grid.append(input())
   
    row_index = 0
    
    row_limit = grid_size-1
    col_limit = grid_size   
    while row_index <row_limit:
        col_index =row_index
        col_limit -=1
        
        while col_index <col_limit:
            temp =[]
            temp.append(grid[row_index][col_index])
            temp.append(grid[col_index][-1-row_index])
            temp.append(grid[-1-row_index][-1-col_index])
            temp.append(grid[-1-col_index][row_index])
            count = defaultdict(int)
            for ele in temp:
                count[ele] +=1
            if count['1'] == 1 or  count['1'] ==3:
                operation_count +=1
            elif count['1'] == 2:                 
                operation_count +=2
            col_index +=1
        row_index +=1
        row_limit -=1
            
    print(operation_count)
            

            
            

            
    # 







