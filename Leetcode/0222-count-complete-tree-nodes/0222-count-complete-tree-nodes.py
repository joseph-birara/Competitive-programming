# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        
        
        def nodeCounter(node):
            if  node:
                return  1+ nodeCounter(node.left)+nodeCounter(node.right) 
            return 0           
            
        
        return nodeCounter(root)
        