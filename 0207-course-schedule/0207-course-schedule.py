class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
       
        color = [0]* numCourses
        stack = []

        for post, pre in prerequisites:
            graph[pre].append(post)
        cycle = [0]
        
        def dfs(node):
            color[node] = 1
            for neighbour in graph[node]:
                if color[neighbour] == 1:
                    cycle[0] = 1
                    return
                if color[neighbour] ==2 :
                    continue
                dfs(neighbour)

            color[node] =2            
            stack.append(node)
        
        for i in range(numCourses):
            if color[i] != 2:
                dfs(i)
            
        
        return  not cycle[0] 
        