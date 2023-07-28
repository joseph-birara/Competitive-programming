from typing import List

class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        def cell_representation(col, row):
            # Convert column number to the alphabetical representation
            col_str = ''
            while col:
                col -= 1
                col_str = chr(ord('A') + col % 26) + col_str
                col //= 26
            return col_str + str(row)

        def generate_cells_in_range(s):
            if ':' not in s:
                raise ValueError("Invalid input format. Expected '<col1><row1>:<col2><row2>'")

            col1row1, col2row2 = s.split(':')
            col1, row1 = col1row1[:-1], col1row1[-1:]
            col2, row2 = col2row2[:-1], col2row2[-1:]

            col1_num = sum((ord(c) - ord('A') + 1) * (26 ** i) for i, c in enumerate(reversed(col1)))
            col2_num = sum((ord(c) - ord('A') + 1) * (26 ** i) for i, c in enumerate(reversed(col2)))
            row1, row2 = int(row1), int(row2)

            cells = []
            for col in range(col1_num, col2_num + 1):
                for row in range(row1, row2 + 1):
                    cells.append(cell_representation(col, row))

            return sorted(cells, key=lambda x: (sum((ord(c) - ord('A') + 1) * (26 ** i) for i, c in enumerate(reversed(x[:-1]))), int(x[-1])))

        return generate_cells_in_range(s)


