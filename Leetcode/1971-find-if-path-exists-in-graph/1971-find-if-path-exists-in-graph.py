class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
       
            
           
        graph = defaultdict(list)
        stack = [source]
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)

        visited = {source}
        while stack :
            vertex = stack.pop()
            if vertex == destination:
                    return True
            for neighbour in graph[vertex]:
                if neighbour not in visited:
                    stack.append(neighbour)
                    visited.add(vertex)
                    
        return False
        
       

        