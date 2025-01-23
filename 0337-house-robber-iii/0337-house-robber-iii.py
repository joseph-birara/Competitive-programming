# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from functools import cache

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        @cache
        def dfs(node):
            if not node:
                return (0, 0)  # (not_rob, rob)

            # Recursively calculate for left and right children
            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this node, we cannot rob its children
            rob = node.val + left[0] + right[0]

            # If we don't rob this node, we take the maximum profit from each child
            not_rob = max(left) + max(right)

            return (not_rob, rob)

        # Get the maximum profit by either robbing or not robbing the root
        return max(dfs(root))
