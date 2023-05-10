n, m = map(int, input().split())
board = [input() for _ in range(n)]
visited = [[False] * m for _ in range(n)]


def dfs(i, j, color):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        if visited[i][j]:
            return True
        visited[i][j] = True
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and board[ni][nj] == color and not visited[ni][nj]:
                stack.append((ni, nj))
    return False


for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if dfs(i, j, board[i][j]):
                print("Yes")
                exit()

print("No")
