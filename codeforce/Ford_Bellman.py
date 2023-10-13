class Graph:
    def __init__(self, numberOfVertices):
        self.V = numberOfVertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        dist = [float("inf")] * self.V
        dist[src] = 0

        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        for i in range(self.V):
            if dist[i] == float("inf"):
                dist[i] = 30000

        print(*dist)


n, m = map(int, input().split())
graph = Graph(n)
for _ in range(m):
    x, y, z = map(int, input().split())
    graph.add_edge(x - 1, y - 1, z)
graph.bellman_ford(0)
