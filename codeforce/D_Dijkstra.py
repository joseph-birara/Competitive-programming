from heapq import *
INFINITY = 1 << 60
num_vertices, num_edges = map(int, input().split())
graph = [[] for _ in range(num_vertices)]
distances = [0] + [INFINITY] * num_vertices
predecessors = [-1] * num_vertices
que = [(0, 0)]

for _ in range(num_edges):
    src, to_, weight = map(int, input().split())
    graph[src - 1] += [(weight, to_ - 1)]
    graph[to_ - 1] += [(weight, src - 1)]

while que:
    vertex = heappop(que)[1]
    for weight, neighbor in graph[vertex]:
        new_distance = distances[vertex] + weight
        if new_distance < distances[neighbor]:
            distances[neighbor], predecessors[neighbor] = new_distance, vertex
            heappush(que,
                     (distances[neighbor], neighbor))

if distances[num_vertices - 1] == INFINITY:
    print(-1)
else:
    vertex, path = num_vertices - 1, []
    while vertex != -1:
        path.append(vertex + 1)
        vertex = predecessors[vertex]
    path.reverse()
    print(' '.join(map(str, path)))
