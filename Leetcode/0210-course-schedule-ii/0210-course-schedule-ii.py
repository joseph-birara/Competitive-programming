class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        graph = defaultdict(list)
        indgree = [0]* numCourses
       
        color = [0]* numCourses
        stack = []
        q = deque()

        for post, pre in prerequisites:
            graph[pre].append(post)
            indgree[post] +=1
        # cycle = [0]
        
#         def dfs(node):
#             color[node] = 1
#             for neighbour in graph[node]:
#                 if color[neighbour] == 1:
#                     cycle[0] = 1
#                     return
#                 if color[neighbour] ==2 :
#                     continue
#                 dfs(neighbour)

#             color[node] =2            
#             stack.append(node)
        
#         for i in range(numCourses):
#             if color[i] != 2:
#                 dfs(i)
            
        
#         return reversed(stack) if not cycle[0] else []


                
                

            
        


        for node in range(numCourses):
            if indgree[node] == 0:
                q.append(node)
        res = []

        while q:
            node = q.popleft()
            res.append(node)
            for post in graph[node]:
                if indgree[post] !=0 :
                    indgree[post] -=1
                if indgree[post] == 0:
                    q.append(post)
            
        return (res) if len(res) ==numCourses else []
