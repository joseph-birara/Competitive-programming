rows, columns = map(int, input().split())
cells = [input() for _ in range(rows)]
visit = [[False] * columns for _ in range(rows)]


def dfs(i, j, color):
    stack = [(i, j)]
    while stack:
        i, j = stack.pop()
        if visit[i][j]:
            return True
        visit[i][j] = True
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = i + di, j + dj
            if 0 <= ni < rows and 0 <= nj < columns and cells[ni][nj] == color and not visit[ni][nj]:
                stack.append((ni, nj))
    return False


for i in range(rows):
    for j in range(columns):
        if not visit[i][j]:
            if dfs(i, j, cells[i][j]):
                print("Yes")
                exit()

print("No")
