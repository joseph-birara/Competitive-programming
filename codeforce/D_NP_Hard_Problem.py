
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
visited = [0] * n

for _ in range(m):
    node, child = map(int, input().split())
    graph[node - 1].append(child - 1)
    graph[child - 1].append(node - 1)

for i in range(n):
    if visited[i]:
        continue
    visited[i] = 1
    queue = [i]

    while queue:
        node = queue.pop()
        for child in graph[node]:
            if visited[child]:
                if visited[child] == visited[node]:
                    print(-1)
                    exit(0)
            else:
                visited[child] = 3 - visited[node]
                queue.append(child)

for i in [1, 2]:
    group_vertices = [str(k + 1) for k, q in enumerate(visited) if q == i]
    print(len(group_vertices))
    print(' '.join(group_vertices))
