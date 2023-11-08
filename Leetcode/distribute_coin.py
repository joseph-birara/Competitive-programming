# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: TreeNode) -> int:
        self.moves = 0

        def dfs(node):
            if not node:
                return 0            
            left = dfs(node.left)
            right = dfs(node.right)
            excess = node.val + left + right - 1            
            self.moves += abs(excess)    
            return excess

        dfs(root)
        return self.moves

        
        
