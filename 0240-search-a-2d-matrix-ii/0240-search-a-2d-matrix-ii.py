

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        for row in matrix :
            for num in row:
                if num == target :
                    return True
        return False
        
#         left = 0
#         right = n * m - 1
        
#         while left <= right:
#             mid = (left + right) // 2
#             mid_value = matrix[mid // n][mid % n]
            
#             if target == mid_value:
#                 return True
#             elif target > mid_value:
#                 left = mid + 1
#             else:
#                 right = mid - 1
        
#         return False
