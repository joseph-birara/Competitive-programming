class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        


        n = len(graph)
        visited = [0] * n  # 0: not visited, 1: visiting, 2: visited
        result = []

        def is_safe(node: int) -> bool:
            if visited[node] == 1:
                return False
            if visited[node] == 2:
                return True

            visited[node] = 1  # Mark node as visiting
            for neighbor in graph[node]:
                if not is_safe(neighbor):
                    return False
            visited[node] = 2  # Mark node as visited
            return True

        for i in range(n):
            if is_safe(i):
                result.append(i)

        return result

        