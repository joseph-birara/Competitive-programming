class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        len_row = len(matrix)
        len_col = len(matrix[0])
        
        temp = []
        
      
        for row in range(len_row):
            for col in range(len_col):
                if matrix[row][col] == 0:
                    temp.append([row,col])
        for i, j in temp:
            for k in range(len_col):
                matrix[i][k] = 0
            for m in range(len_row):
                matrix[m][j] = 0
                