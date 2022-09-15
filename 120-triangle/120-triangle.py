class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        for i in range(1,m):
            triangle[i][0]+=triangle[i-1][0]
            triangle[i][-1]+=triangle[i-1][-1]
        for i in range(2,m):
            for j in range(1,i):
                triangle[i][j]+=min(triangle[i-1][j-1], triangle[i-1][j])
        print(triangle)
        return min(triangle[-1])
                
            
            
        
        