from collections import defaultdict
from typing import Iterable, List

class Solution:
    def getAncestors(self, num_nodes: int, edges: List[List[int]]) -> Iterable[List[int]]:
        def dfs(node: int) -> set:
            if not ancestors[node]:
                for adj_node in graph[node]:
                    if adj_node not in ancestors[node]:
                        ancestors[node].update({adj_node} | dfs(adj_node))
            return ancestors[node]

        graph = defaultdict(set)
        for parent, child in edges:
            graph[child].add(parent)

        ancestors = [set() for _ in range(num_nodes)]
        for node in range(num_nodes):
            if not ancestors[node]:
                dfs(node)

        return map(sorted, ancestors)
