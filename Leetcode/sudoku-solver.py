from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.solve(board)

    def solve(self, board):
        # Find the first empty cell
        empty_cell = self.find_empty(board)
        
        # If no empty cell is found, the board is solved
        if not empty_cell:
            return True
        
        row, col = empty_cell

        # Try placing numbers 1 to 9 in the empty cell
        for num in map(str, range(1, 10)):
            if self.is_valid(board, row, col, num):
                # Place the number if it's valid
                board[row][col] = num

                # Recursively try to solve the rest of the board
                if self.solve(board):
                    return True

                # If placing the current number doesn't lead to a solution, backtrack
                board[row][col] = '.'

        # No valid number was found, backtrack
        return False

    def find_empty(self, board):
        # Find the first empty cell (denoted by '.')
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    return (i, j)
        return None

    def is_valid(self, board, row, col, num):
        # Check if the number is not present in the same row, column, or 3x3 subgrid
        return (
            self.is_valid_row(board, row, num) and
            self.is_valid_col(board, col, num) and
            self.is_valid_subgrid(board, row, col, num)
        )

    def is_valid_row(self, board, row, num):
        return num not in board[row]

    def is_valid_col(self, board, col, num):
        return num not in [board[i][col] for i in range(9)]

    def is_valid_subgrid(self, board, row, col, num):
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False
        return True


        


    

    def check(self, matrix):
        
        for row in matrix:
            if len(set(row)) != 9:
                return False

        # Check each column
        for col in range(9):
            column_elements = set(matrix[row][col] for row in range(9))
            if len(column_elements) != 9:
                return False

        # Check each 3x3 subgrid
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                subgrid_elements = set(matrix[x][y] for x in range(i, i + 3) for y in range(j, j + 3))
                if len(subgrid_elements) != 9:
                    return False

        # If all checks pass, the matrix is valid
        return True

        


        