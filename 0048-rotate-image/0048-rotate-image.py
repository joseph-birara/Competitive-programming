class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        
        approach
        tanspos then swap colums
        """
        matrix_len = len(matrix)
        
        
        # transpose
        
        for row in range(matrix_len):
            for col in range(row,matrix_len):
                matrix[row][col],matrix[col][row] = matrix[col][row],matrix[row][col]
        
        # swap columns
        
        left = 0
        right = matrix_len-1
        while left<right:
            for one_row in range(matrix_len):
                matrix[one_row][left],  matrix[one_row][right] = matrix[one_row][right], matrix[one_row][left]  
            left +=1
            right -=1