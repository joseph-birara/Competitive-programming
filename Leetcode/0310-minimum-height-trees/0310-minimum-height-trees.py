class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        pass
        # def dfs(curr,node):
        #     for nei in graph[node]:
        if not edges:
            return [0]
        

        graph = defaultdict(list)

        indgree = [0] *n
        for parent , child in edges:
            indgree[parent] += 1
            indgree[child] += 1
            graph[parent].append(child)
            graph[child].append(parent)

        
        q = deque()
        leaves = []
             
        
        for node in range(n):
            if indgree[node]  == 1:
                q.append(node)
                

        while n >2 : 
                             
                
            for node in q:                              
                for nei in graph[node]:                
                    indgree[nei] -=1                    
                    if indgree[nei] == 1:
                        leaves.append(nei)
            n -= len(q)
            q = leaves[:]
            leaves = []
            
                        
        
        return q
                       

    

        




                