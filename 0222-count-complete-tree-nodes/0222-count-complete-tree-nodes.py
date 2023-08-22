# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        
        res = [0]
        
        def nodeCounter(node):
            if not node:
                return 
            res[0]+=1
            nodeCounter(node.left)
            nodeCounter(node.right)
            
        nodeCounter(root)
        return res[0]
        