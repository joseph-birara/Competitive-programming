# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = defaultdict(TreeNode)
        
        def make_parent(node,parent):
            if not node:
                return 
            graph[node]= parent               
            
            make_parent(node.right,node)
            make_parent(node.left,node)
        
        
        make_parent(root,None)
        
        q = deque()
        q.append((target.val,0))
        res = []
        visited = set()  
       
        
        def dfs(node,distance):
            if  not node or node.val in visited or distance > k :
                return 
            visited.add(node.val)
            if distance == k:
                res.append(node.val)
            
            dfs(node.left,distance +1)
            dfs(node.right,distance +1)
            dfs(graph[node],distance +1)
        
        dfs(target,0)        
            
        return res
                
        
        
            
            
            
                
        