class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        graph = defaultdict(list)

        for index, ab in enumerate(equations):
            num, denum = ab[0], ab[1]
            graph[num].append((denum,values[index]))
            graph[denum].append((num,1/values[index]))
        
        def bfs(src, dest):
            if src not in graph or dest not in graph:
                return -1.0
            visited = set()
            que = deque()

            que.append((src,1))
            visited.add(src)

            while que:
                node, value = que.popleft()
                if node == dest:
                    return value
                for nei in graph[node]:
                    if nei[0] not in visited:
                        que.append((nei[0],value*nei[1]))
                        visited.add(nei[0])
            return -1.0
        
        return [bfs(query[0],query[1]) for index, query in enumerate(queries)]
            
        
