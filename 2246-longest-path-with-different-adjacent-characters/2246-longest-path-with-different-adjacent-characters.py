class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        answer = [0] 
        n = len(parent)  
        graph = [[] for _ in range(n)]  

        # build the graph
        for i in range(n):
            if parent[i] != -1:
                graph[parent[i]].append(i)  

        
        def dfs(node):
            
            longest = 0
            second_longest = 0
            
            for v in graph[node]:
                val = dfs(v)
                # if the character of node u is different from the character of node v
                if s[node] != s[v]:
                    # update the longest and second longest paths accordingly
                    if val > second_longest:
                        second_longest = val
                    if second_longest > longest:
                        longest, second_longest = second_longest, longest
            # update the answer with the longest path that includes node u
            answer[0] = max(answer[0], longest + second_longest + 1)
            # return the longest path from node u
            return longest + 1

        # call dfs on the root node (0)
        dfs(0)

        return answer[0]
