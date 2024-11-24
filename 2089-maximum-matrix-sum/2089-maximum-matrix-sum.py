class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        abs_sum = 0
        min_abs = float('inf')
        negative_count = 0

        # Step 1: Calculate abs_sum, min_abs, and negative_count
        for i in range(n):
            for j in range(n):
                abs_sum += abs(matrix[i][j])
                if matrix[i][j] < 0:
                    negative_count += 1
                min_abs = min(min_abs, abs(matrix[i][j]))

        # Step 2: Adjust based on negative parity
        if negative_count % 2 != 0:
            abs_sum -= 2 * min_abs

        return abs_sum

                

        
        