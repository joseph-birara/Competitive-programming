class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        
        n = len (matrix)
        m = len(matrix[0])
        
        heap = []
        
        for i in range (n):
            for j in range(m):
                heappush(heap,-matrix[i][j])
                if len(heap) > k:
                    heappop(heap)
        return -heappop(heap)
                
        