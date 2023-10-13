class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        
        graph = defaultdict(list)
        i = 0
        for fro, to in edges:
            graph[fro].append((to,succProb[i]))
            graph[to].append((fro,succProb[i]))
            i += 1        


        def dijkstra(graph, start):
            distances = {node: 0 for node in range(n)}
            distances[start] = 1
            visited = set()
            priority_queue = deque([start])

            while priority_queue:
                current_node =  priority_queue.popleft()         

                for neighbor, weight in graph[current_node]:
                    distance = distances[current_node] * weight
                    if distance > distances[neighbor]:
                        distances[neighbor] = distance
                        priority_queue.append(neighbor)
           

            return distances[end_node]
        return dijkstra(graph, start_node)
        
