class Solution:
       
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
  
        if (len(matrix) == 0):
            return result

        m = len(matrix)
        n = len(matrix[0])
        visited = [[0 for i in range(n)] for j in range(m)]
        dr = [0, 1, 0, -1] # rirection of row
        dc = [1, 0, -1, 0] # direction of column
        x = 0
        y = 0
        di = 0 #current direction

        # Iterate from 0 to R * C - 1
        for i in range(m * n):
            result.append(matrix[x][y])
            visited[x][y] = True
            cr = x + dr[di] #current row
            cc = y + dc[di]

            if (0 <= cr and cr < m and 0 <= cc and cc < n and not(visited[cr][cc])):
                x = cr
                y = cc
            else:
                di = (di + 1) % 4
                x += dr[di]
                y += dc[di]
        return result
        