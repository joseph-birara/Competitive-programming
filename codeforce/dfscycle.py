def isCycleUtil(adj, visited, u, parent):
    visited[u] = True
    for v in adj[u]:
        if not visited[v]:
            if isCycleUtil(adj, visited, v, u):
                return True
        elif v != parent:
            return True
    return False


def isCycle(adj, V):
    visited = [False] * V
    for i in range(V):
        if not visited[i]:
            if isCycleUtil(adj, visited, i, -1):
                return True
    return False
