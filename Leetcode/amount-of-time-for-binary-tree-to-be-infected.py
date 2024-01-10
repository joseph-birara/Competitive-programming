# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:

        # form undirected graph
        # run bfs 
        graph = defaultdict(list)
        visited = set()
        def dfs(parent,node):
            if not node:
                return
            if parent:          
                graph[parent.val].append(node.val)
                graph[node.val].append(parent.val)
            dfs(node,node.left)
            dfs(node,node.right)
        dfs(None,root)

        minutes = [0]

        def bfs(node):
            q = deque([(node,0)])
            visited.add(node)
            while q:
                curr,dist = q.popleft()
                for nei in graph[curr]:
                    if nei not in visited:
                        q.append((nei,dist+1))
                        visited.add(nei)
                minutes[0] = max(minutes[0], dist+1)
        bfs(start)

        return minutes[0]-1

        

            
            
        