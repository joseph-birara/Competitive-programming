def find_negative_cycle(graph, n):
    dist = [0] * n
    parent = [-1] * n

    x = -1
    for i in range(n):
        x = -1
        for u, v, w in graph:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                parent[v] = u
                x = v

    if x == -1:
        return "NO"

    for _ in range(n):
        x = parent[x]

    cycle = [x]
    y = parent[x]
    while y != x:
        cycle.append(y)
        y = parent[y]
    cycle.append(x)

    return "YES\n" + " ".join(str(node + 1) for node in reversed(cycle))


n, m = map(int, input().split())
graph = []
for _ in range(m):
    a, b, c = map(int, input().split())
    graph.append((a - 1, b - 1, c))

result = find_negative_cycle(graph, n)
print(result)
