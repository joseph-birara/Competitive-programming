
class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        graph = defaultdict(list)
        count = [0] * n
        memo = {}

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def contribution(start, end):
            count[start] += 1
            visited.add(start)

            if start == end:
                return True

            for adj in graph[start]:
                if adj not in visited and contribution(adj, end):
                    return True

            count[start] -= 1
            return False

        for a, b in trips:
            visited = set()
            contribution(a, b)

        def dp(node, parent, isHalved):
            if (node, isHalved) in memo:
                return memo[(node, isHalved)]

            res1 = inf
            res2 = price[node] * count[node]

            if not isHalved:
                res1 = (price[node] // 2) * count[node]

                for adj in graph[node]:
                    if parent != adj:
                        res1 += dp(adj, node, True)

            for adj in graph[node]:
                if parent != adj:
                    res2 += dp(adj, node, False)

            memo[(node, isHalved)] = min(res1, res2)

            return memo[(node, isHalved)]

        return dp(0, -1, False)
