class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for k in i:
                if k == target:
                    return True
        return False
        