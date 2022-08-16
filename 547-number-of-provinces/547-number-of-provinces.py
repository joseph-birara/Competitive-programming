class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        provinces = len(isConnected)
        visited = set()
        circles = 0
        
        for i in range(provinces):
            if i not in visited:
                Q = collections.deque([i])
                while Q:
                    j = Q.popleft()
                    visited.add(j)
                    for k in range(provinces):
                        if isConnected[j][k] == 1 and k not in visited:
                            Q.append(k)
                circles += 1
        
        return circles
        
        
        