class Solution:
    def minCost(self, grid: List[List[int]]) -> int:


        m, n = len(grid), len(grid[0])
        directions = {1: (0, 1), 2: (0, -1), 3: (1, 0), 4: (-1, 0)}
        
        # Cost matrix initialized to infinity
        cost = [[float('inf')] * n for _ in range(m)]
        cost[0][0] = 0

        # 0-1 BFS
        deque_q = deque([(0, 0)])  # (row, col)
        
        while deque_q:
            x, y = deque_q.popleft()
            # If we've reached the bottom-right corner
            if (x, y) == (m - 1, n - 1):
                return cost[x][y]
            
            for dir_idx, (dx, dy) in directions.items():
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n:
                    new_cost = cost[x][y] + (1 if grid[x][y] != dir_idx else 0)
                    if new_cost < cost[nx][ny]:
                        cost[nx][ny] = new_cost
                        if grid[x][y] == dir_idx:
                            deque_q.appendleft((nx, ny))  # Prefer cells with no cost
                        else:
                            deque_q.append((nx, ny))  # Process modified cells later
        
        return cost[m - 1][n - 1]
