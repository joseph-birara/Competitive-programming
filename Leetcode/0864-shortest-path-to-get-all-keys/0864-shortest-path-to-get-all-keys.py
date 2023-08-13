import collections

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        start_point = None
        num_keys = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '@':
                    start_point = [r, c]
                if grid[r][c] in 'abcdef':
                    num_keys += 1
        
        queue = collections.deque([(start_point[0], start_point[1], '')])
        visited = set()
        directions = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        steps = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, collected_keys = queue.popleft()
                if (x, y, collected_keys) in visited:
                    continue
                if len(collected_keys) == num_keys:
                    return steps
                
                visited.add((x, y, collected_keys))

                for dx, dy in directions:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] != '#':
                        cell = grid[nx][ny]
                        if cell in 'ABCDEF' and cell.lower() in collected_keys:
                            queue.append((nx, ny, collected_keys))
                        elif cell in '.@':
                            queue.append((nx, ny, collected_keys))
                        elif cell in 'abcdef':
                            if cell not in collected_keys:
                                queue.append((nx, ny, collected_keys + cell))
                            else:
                                queue.append((nx, ny, collected_keys))
            
            steps += 1

        return -1


