# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        tilt = 0
        def tiFind(root):
            
            nonlocal tilt
            if (not root):
                return 0  
            left = tiFind(root.left)
            right = tiFind(root.right)

            # Add current tilt to overall
            tilt += abs(left - right)

            return left + right + root.val
        
        tiFind(root)
        return tilt
        
        