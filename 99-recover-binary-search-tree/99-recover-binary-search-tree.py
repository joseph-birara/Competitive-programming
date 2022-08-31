# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        temp = []
        def inorder(node):
            if not node: return
            inorder(node.left)
            temp.append(node)
            inorder(node.right)
        inorder(root)
        srt = sorted(m.val for m in temp)
        for i in range(len(temp)):
            temp[i].val = srt[i]
        