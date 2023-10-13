import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
        graph = [[] for _ in range(n)]
        for frm, to, cost in flights:
            graph[frm].append((cost, to))    
        pq = [(0, 0, src)]
        heapq.heapify(pq)
     
        cheapest_cost_stops = [(float("inf"), float("inf"))] * n
        cheapest_cost_stops[src] = (0, 0)

        while pq:
            cost, stops, node = heapq.heappop(pq)           
            if node == dst:
                return cost           
            if stops <= k:
                for ct, to in graph[node]:
                    new_cost = cost + ct
                    new_stops = stops + 1                   
                    if new_cost < cheapest_cost_stops[to][0] or new_stops < cheapest_cost_stops[to][1]:
                        cheapest_cost_stops[to] = (new_cost, new_stops)
                        heapq.heappush(pq, (new_cost, new_stops, to))

       
        return -1
