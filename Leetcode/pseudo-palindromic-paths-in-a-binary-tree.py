# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def dfs(node, myhash):
            if node:
                myhash[node.val] += 1

                if not node.left and not node.right:
                    odd_count = sum(1 for count in myhash.values() if count % 2 == 1)
                    res[0] += odd_count < 2

                dfs(node.left, myhash.copy())
                dfs(node.right, myhash.copy())

        res = [0]
        dfs(root, Counter())
        return res[0]
        