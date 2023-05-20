
from collections import deque


def nearestExit(maze,  entrance):
    def in_bound(row, col):
        return 0 <= row < row_len and 0 <= col < col_len

    visited = set((0, 0))
    dirxns = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    q = deque([(entrance[0], entrance[1], 0)])

    row_len = len(maze)
    col_len = len(maze[0])

    while q:
        row, col, distance = q.popleft()

        if (row == row_len - 1 or col == col_len - 1 or row == 0 or col == 0) and [row, col] != entrance:
            return distance

        for x, y in dirxns:
            new_row = row + x
            new_col = col + y
            if (new_row, new_col) not in visited and in_bound(new_row, new_col) and maze[new_row][new_col] == '.':
                q.append((new_row, new_col, distance+1))
                visited.add((new_row, new_col))

    return -1
