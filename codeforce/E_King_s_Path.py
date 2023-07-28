from collections import deque


def main():
    # Input
    x0, y0, x1, y1 = map(int, input().split())
    n = int(input())
    allowed = set()
    for i in range(n):
        r, a, b = map(int, input().split())
        for i in range(a, b + 1):
            allowed.add((r, i))

    # BFS
    queue = deque([(x0, y0)])
    visited = set([(x0, y0)])
    neighbors = [[-1, 0], [0, -1], [0, 1], [1, 0],
                 [-1, 1], [1, -1], [1, 1], [-1, -1]]
    level = 0
    while queue:
        level += 1
        for _ in range(len(queue)):
            x, y = queue.popleft()
            if (x, y) == (x1, y1):
                return level - 1
            for dx, dy in neighbors:
                nx, ny = x + dx, y + dy
                if (nx, ny) in allowed and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    queue.append((nx, ny))

    # No path found
    return -1


print(main())
