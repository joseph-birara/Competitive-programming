class Graph:
    def __init__(self, numberOfVertices):
        self.V = numberOfVertices
        self.graph = []

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, src):
        # Step 1: Initialize distances
        dist = [float("inf")] * self.V
        dist[src] = 0

        # Step 2: Iterative Relaxation (N-1 times)
        for _ in range(self.V - 1):
            for u, v, w in self.graph:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w

        # Step 3: Detect Negative Cycles
        for u, v, w in self.graph:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                print("Negative Cycle Detected")
                return

        # Step 4: Output Results
        print(dist)
