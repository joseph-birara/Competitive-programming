from typing import List
class Solution:
    
    def isCycleUtil(self,adj, visited, u, parent):
        visited[u] = True
        for v in adj[u]:
            if not visited[v]:
                if self.isCycleUtil(adj, visited, v, u):
                    return True
            elif v != parent:
                return True
        return False
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		#Code here
		visited = [False] * V
        for i in range(V):
            if not visited[i]:
                if self.isCycleUtil(adj, visited, i, -1):
                    return True
        return False
        
                
            
                    
            
            
            
            
                
        
        
        
        
        
        
       
        
        
       
            
        
        return   


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends