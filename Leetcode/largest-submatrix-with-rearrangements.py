class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:

        n = len(matrix)
        m = len(matrix[0])

        ans = 0

        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0 and i > 0:
                    matrix[i][j] += matrix[i-1][j]
            

            curr_row = sorted(matrix[i], reverse = True)

            for k in range(m):
                ans = max(ans, curr_row[k] * (k+1))

        return ans

        