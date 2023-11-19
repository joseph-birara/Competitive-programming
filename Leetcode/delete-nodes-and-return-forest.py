# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)
        def dfs(node):
            if not node :
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)

            if node.val in to_delete:
                if not node.left and not node.right:
                    return None
                if node.left:
                    res.append(node.left)
                if node.right:
                    res.append(node.right)
                return None
            return node
        

        res = []

        node = dfs(root)

        if node :
            res.append(node)
        return res

        