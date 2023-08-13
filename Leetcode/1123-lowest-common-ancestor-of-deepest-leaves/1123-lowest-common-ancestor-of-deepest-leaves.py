# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def finddepth(root):            
            if (not root):
                return 0            
            left = finddepth(root.left)

            right = finddepth(root.right)            
            return 1 + max(left, right)          
        def dfs(root, curr, depth):           
            if (not root):
                return None
            if (curr == depth):
                return root           
            left = dfs(root.left, curr + 1, depth)           
            right = dfs(root.right, curr + 1, depth)           
            if (left != None and right != None):
                return root          
          
            return left if left else right
        
        if (not root):
            return None      
        depth = finddepth(root) - 1      
        return dfs(root, 0, depth)
        
        
        
        