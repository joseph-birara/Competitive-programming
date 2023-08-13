class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
          
        #function to check if it is magic swuare
        
        def check_magic(square,row ,col):
            
            first_row = square[row][col] +square[row][col+1] +square[row][col+2]
            second_row = square[row+1][col] +square[row+1][col+1] +square[row+1][col+2]
            third_row = square[row+2][col] +square[row+2][col+1] +square[row+2][col+2]
            
            first_col = square[row][col] +square[row+1][col] +square[row+2][col]
            
            second_col = square[row][col+1] +square[row+1][col+1] +square[row+2][col+1]
            
            third_col = square[row][col+2] +square[row+1][col+2] +square[row+2][col+2]
            
            main_diagonal = square[row][col] +square[row+1][col+1] +square[row+2][col+2]
            right_diagonal = square[row][col+2] +square[row+1][col+1] +square[row+2][col]
            
           
            temp = []
            for i in range(3):
                for j in range(3):
                    if square[row+i][col+j] > 9 or square[row+i][col+j]<1:
                        return False
                    temp.append(square[row+i][col+j])
            if len(set(temp)) == 9 and main_diagonal==right_diagonal == third_col ==second_col ==first_col == third_row ==second_row ==first_row :
                return True
            return False
        
        row = len(grid)
        col = len(grid[0])
        magic_count =0
        
        for row_index in range(row-2):
            for col_index in range(col-2):
                if check_magic(grid,row_index,col_index) == True:
                    magic_count +=1
        return magic_count
        
        
        
        

                