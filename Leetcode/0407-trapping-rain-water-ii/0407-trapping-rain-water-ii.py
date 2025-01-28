class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
    
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        heap = []
        
        # Add all boundary cells to the heap
        for i in range(m):
            for j in range(n):
                if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = True
        
        # Directions for 4-connected neighbors
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        trapped_water = 0
        
        while heap:
            height, x, y = heapq.heappop(heap)
            
            # Explore neighbors
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]:
                    # Water trapped is the difference between current boundary height and neighbor height
                    trapped_water += max(0, height - heightMap[nx][ny])
                    # Update the height of the neighbor to maintain the boundary
                    heapq.heappush(heap, (max(height, heightMap[nx][ny]), nx, ny))
                    visited[nx][ny] = True
        
        return trapped_water
            