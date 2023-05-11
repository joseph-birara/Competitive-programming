# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(list)
        
        def dfs(node):
            if not node:
                return 
            if node.left:
                graph[node.val].append(node.left.val)
                graph[node.left.val].append(node.val)
            if node.right:
                graph[node.val].append(node.right.val)
                graph[node.right.val].append(node.val)       
                               
            
            dfs(node.right)
            dfs(node.left)
        
        
        dfs(root)
        
        q = deque()
        q.append((target.val,0))
        res = []
        visited = set()  
        visited.add(target.val)
        
        while q :
            node, distance = q.popleft()
            if distance == k:
                res.append(node)
            for val in graph[node]:
                if val not in visited :
                    visited.add(val)
                    q.append((val,distance +1))
        return res
                
        
        
            
            
            
                
        