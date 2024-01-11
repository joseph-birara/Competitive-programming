# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        res = [0]
        def dfs(node):
            if not node:
                return [float('-inf'),float('inf')]
            if not node.right and not node.left:
                return [node.val,node.val]
            left = dfs(node.left)
            right = dfs(node.right)

            max_tmp = max(left[0],right[0])
            min_tmp = min(left[1],right[1])
            res[0] = max(res[0],abs(node.val-max_tmp), abs(node.val-min_tmp))

            return [max(node.val,max_tmp), min(node.val, min_tmp)]
        dfs(root)
        return res[0]





        