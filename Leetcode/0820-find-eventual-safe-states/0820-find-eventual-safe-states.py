from collections import defaultdict, deque
from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Step 1: Build the reverse graph and calculate in-degrees
        n = len(graph)
        reverse_graph = defaultdict(list)
        in_degree = [0] * n
        
        for node in range(n):
            for neighbor in graph[node]:
                reverse_graph[neighbor].append(node)
                in_degree[node] += 1
        
        # Step 2: Start with terminal nodes (in-degree 0)
        queue = deque([node for node in range(n) if in_degree[node] == 0])
        safe_nodes = []
        
        # Step 3: Perform BFS to find safe nodes
        while queue:
            node = queue.popleft()
            safe_nodes.append(node)
            for parent in reverse_graph[node]:
                in_degree[parent] -= 1
                if in_degree[parent] == 0:
                    queue.append(parent)
        
        # Step 4: Return sorted list of safe nodes
        return sorted(safe_nodes)
