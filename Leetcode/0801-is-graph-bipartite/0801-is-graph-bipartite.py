class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1]*n

        def dfs(node,c):
            color[node] = c
            for nei in graph[node]:
                if color[nei] == -1:
                    if not dfs(nei,1-c) :
                        return False
                if color[nei] == c:
                    return False
            return True
        for i in range(n):
            if color[i] == -1 and not dfs(i, 0):
                return False
        return True

        