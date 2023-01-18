class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        formated_string_array = []
        
        for row in range(9):
            for col in range(9):
                element = board[row][col]
                if element !='.':
                    
                    formated_string_array.append(f"{element}in {row}th row")
                    formated_string_array.append(f"{element}in {col}ih column")
                    formated_string_array.append(f"{element}in {row//3},{col//3} Square-board")
        return len(formated_string_array) == len(set(formated_string_array))
                
                
        