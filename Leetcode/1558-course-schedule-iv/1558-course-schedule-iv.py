class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        # Initialize the reachability matrix
        reachable = [[False] * numCourses for _ in range(numCourses)]
        
        # Populate the direct prerequisites
        for a, b in prerequisites:
            reachable[a][b] = True
        
        # Compute transitive closure using Floyd-Warshall
        for k in range(numCourses):
            for i in range(numCourses):
                for j in range(numCourses):
                    if reachable[i][k] and reachable[k][j]:
                        reachable[i][j] = True
        
        # Answer the queries
        result = []
        for u, v in queries:
            result.append(reachable[u][v])
        
        return result
