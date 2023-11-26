class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        graph = defaultdict(list)       

        for src , dest in tickets :
            graph[src].append(dest)
                      
        for key in graph:
           heapify(graph[key])
        
        res = []
        

        def dfs(node):       
           
            while graph[node]:                
                dfs(heappop(graph[node]))
            res.append(node)
        
        dfs("JFK")
        return res[::-1]







        