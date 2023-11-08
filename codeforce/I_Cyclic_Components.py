

from collections import defaultdict


n, m,  = map(int, input().split())
graph = defaultdict(list)

for i in range(m):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
