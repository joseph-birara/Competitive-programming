class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n , m = len(obstacleGrid), len(obstacleGrid[0])
        
        if n == m and n == 1 and obstacleGrid[0][0] == 1:
            return 0
        
        dp = [[0]*(m) for i in range(n)]
        
        dp[0][0] = 1
        
        
        for i in range(n):
            for j in range(m):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        for i in range(n):
            for j in range(m):                
                if obstacleGrid[i][j] != -1:
                    if i >= 1 and j >=1:
                        temp = 0
                        if obstacleGrid[i-1][j] != -1:
                            temp += dp[i-1][j]
                        if obstacleGrid[i][j-1] != -1:
                            temp += dp[i][j-1]
                        dp[i][j] = temp
                    elif i >= 1 and obstacleGrid[i-1][j] != -1:
                        dp[i][j] = dp[i-1][j]
                    elif j >= 1 and obstacleGrid[i][j-1] != -1:
                        dp[i][j] = dp[i][j-1] 
                    
                        
        return dp[n-1][m-1]
                    
                
                
                
        
        
        