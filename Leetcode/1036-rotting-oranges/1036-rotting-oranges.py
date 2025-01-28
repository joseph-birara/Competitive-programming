
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        # Initialize variables
        fresh_count = 0
        rotten_queue = deque()
        
        # Identify all rotten oranges and count fresh oranges
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_count += 1
                elif grid[r][c] == 2:
                    rotten_queue.append((r, c))
        
        # BFS to spread rotting
        minutes = 0
        while rotten_queue and fresh_count > 0:
            for _ in range(len(rotten_queue)):
                x, y = rotten_queue.popleft()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        # Rot the fresh orange
                        grid[nx][ny] = 2
                        fresh_count -= 1
                        rotten_queue.append((nx, ny))
            minutes += 1
        
        # If there are still fresh oranges, return -1
        return minutes if fresh_count == 0 else -1
