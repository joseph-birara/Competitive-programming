
from math import inf

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for source, dest, time in times:
            graph[source - 1].append((dest - 1, time))

        def dijkstra(graph, start):
            distances = [inf] * n
            distances[start] = 0
            visited = set()
            priority_queue = [(0, start)]

            while priority_queue:
                current_distance, current_node = heapq.heappop(priority_queue)

                if current_node in visited:
                    continue

                visited.add(current_node)

                for neighbor, weight in graph[current_node]:
                    distance = current_distance + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))

            return distances

        arr = dijkstra(graph, k - 1)
        res = max(arr)

        if res == float('inf'):
            return -1
        else:
            return res
