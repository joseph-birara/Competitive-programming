

class Solution:
    def restoreArray(self, adjacentPairs):
        
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)

        
        visited = set()
        result = []

        def dfs(node):
            visited.add(node)
            result.append(node)

            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        
        vertices = [x for x in graph if len(graph [x]) == 1]
        dfs(vertices[0])

        return result
