from typing import List

class Solution:
    def allCellsDistOrder(self, rows: int, cols: int, rCenter: int, cCenter: int) -> List[List[int]]:
        def calculate_distance(r1, c1, r2, c2):
            return abs(r1 - r2) + abs(c1 - c2)

        result = []
        for r in range(rows):
            for c in range(cols):
                result.append([r, c])

        result.sort(key=lambda cell: calculate_distance(cell[0], cell[1], rCenter, cCenter))
        return result


