from collections import Counter, defaultdict


testtCase = int(input())

for _ in range(testtCase):
    num_vertiece, num_edges = map(int, input().split())
    graph = defaultdict(list)

    for i in range(num_edges):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)
    visited = [0] * (num_vertiece + 1)
    leaf, x, y = 0, 0, 0

    for key in graph:
        if len(graph[key]) == 1:
            leaf = key
            break

    y = len(graph[graph[leaf][0]])
    parent = graph[leaf][0]

    for key in graph[graph[leaf][0]]:
        x = max(x, len(graph[key]))
    print(x, y-1)
