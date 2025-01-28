# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:

        @cache
        def dfs(node, status):
            if not node:
                return 0
            if status:
                return dfs(node.left, False) + dfs(node.right,False)
            else:
                rob = node.val + dfs(node.left, True) + dfs(node.right,True)
                skip = dfs(node.left, False) + dfs(node.right,False)
                return max(rob,skip)
        
        return max(dfs(root,False), dfs(root, True))
        