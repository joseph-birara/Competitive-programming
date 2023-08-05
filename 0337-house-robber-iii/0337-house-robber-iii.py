# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        memo = {}

        def rob_amount(node: TreeNode, parent_robbed: bool) -> int:
            if not node:
                return 0

            if (node, parent_robbed) in memo:
                return memo[(node, parent_robbed)]

            if parent_robbed:
                amount = rob_amount(node.left, False) + rob_amount(node.right, False)
            else:
                with_node = node.val + rob_amount(node.left, True) + rob_amount(node.right, True)
                without_node = rob_amount(node.left, False) + rob_amount(node.right, False)
                amount = max(with_node, without_node)

            memo[(node, parent_robbed)] = amount
            return amount

        return rob_amount(root, False)

        