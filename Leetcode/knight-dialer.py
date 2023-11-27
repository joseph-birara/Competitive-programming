class Solution:
    def knightDialer(self, n: int) -> int:
        def in_bound(row,col):
            return 0<=row < 4 and 0 <= col < 3 and (row,col) != (3,0) and (row,col) != (3,2)

              
        drxn = [(-1,2),(-1,-2),(1,-2),(1,2),(2,1),(2,-1),(-2,1),(-2,-1)]
        res = 0

        @cache
        def dfs(left,i,j):
            if left == 1:               
                return 1
            total = 0
            for x, y in drxn:
                if in_bound(i + x, j + y):
                    total += dfs(left - 1, i + x, j + y)
            return total % (10**9 + 7)
            
        for i in range(4):
            for j in range(3):
                if in_bound(i,j):
                    res += dfs(n,i,j)
        return res % (10**9 + 7)
                
                







        