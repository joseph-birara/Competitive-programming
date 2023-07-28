
from collections import defaultdict, deque


num_vetices, num_edges = map(int, input().split())

graph = defaultdict(list)
edges = []
colors = [-1] * (num_vetices + 1)

for _ in range(num_edges):
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)
    edges.append((u, v))

colors[1] = 0
q = deque()
q.append(1)

while q:
    node = q.popleft()
    for nei in graph[node]:
        if colors[nei] == -1:
            colors[nei] = 1 - colors[node]
            q.append(nei)
        elif colors[nei] == colors[node]:
            print("NO")
            exit()
print("YES")

for (u, v) in edges:
    if colors[u] == 0:
        print(1, end="")
    else:
        print(0, end="")

print()
