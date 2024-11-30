class Solution:
    def validArrangement(self, pairs: List[List[int]]) -> List[List[int]]:       

       
        graph = defaultdict(list)
        edge_count = defaultdict(int)

        for start, end in pairs:
            graph[start].append(end)
            edge_count[start] += 1
            edge_count[end] -= 1
        
        
        root = pairs[0][0]
        ans = []
        for node in edge_count:
            if edge_count[node] == 1:
                root = node
                break
        
        
        def dfs(node):
            while graph[node]:
                next_node = graph[node].pop()
                dfs(next_node)
                ans.append([node,next_node])

        
        dfs(root)       

        
        return ans[::-1]
