def isCycle(adj, V):
    visited = [False] * V
    parent = [-1] * V
    for i in range(V):
        if not visited[i]:
            queue = [i]
            visited[i] = True
            while queue:
                u = queue.pop(0)
                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        queue.append(v)
                        parent[v] = u
                    elif parent[u] != v:
                        return True
    return False
