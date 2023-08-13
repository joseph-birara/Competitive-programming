from typing import List
from collections import defaultdict

class Solution:
    def minimumTime(self, n: int, m: int, edges: List[List[int]]) -> List[int]:
        # Build the adjacency list representation of the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
        
        # Initialize the indegree array to track the number of incoming edges for each node
        indegree = [0] * (n + 1)
        
        # Calculate the indegrees of all nodes
        for u, v in edges:
            indegree[v] += 1
        
        # Initialize the time array to store the minimum time for each job
        time = [1] * (n + 1)
        
        # Perform topological sort using a queue
        queue = []
        for u in range(1, n + 1):
            if indegree[u] == 0:
                queue.append(u)
        
        while queue:
            u = queue.pop(0)
            
            # Process the neighbors of the current node
            for v in graph[u]:
                indegree[v] -= 1
                time[v] = max(time[v], time[u] + 1)
                
                if indegree[v] == 0:
                    queue.append(v)
        
        return time[1:]


        



#{ 
 # Driver Code Starts
class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()



class IntMatrix:
    def __init__(self) -> None:
        pass
    def Input(self,n,m):
        matrix=[]
        #matrix input
        for _ in range(n):
            matrix.append([int(i) for i in input().strip().split()])
        return matrix
    def Print(self,arr):
        for i in arr:
            for j in i:
                print(j,end=" ")
            print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=IntArray().Input(2)
        
        
        edges=IntMatrix().Input(a[1], a[1])
        
        obj = Solution()
        res = obj.minimumTime(a[0],a[1], edges)
        
        IntArray().Print(res)
        

# } Driver Code Ends