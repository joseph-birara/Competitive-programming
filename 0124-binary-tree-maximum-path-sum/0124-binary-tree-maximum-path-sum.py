# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        global_max = [root.val]

        def dfs(root):
            if not root :
                return 0

            leftMax = max(0, dfs(root.left))
            rightMax = max(0, dfs( root.right))

            local_max = root.val + leftMax + rightMax

            global_max[0] = max(global_max[0], local_max)

            return  root.val + max( leftMax, rightMax)
        
        dfs(root)

        return global_max[0]
        