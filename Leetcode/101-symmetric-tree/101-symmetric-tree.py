# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.tester(root,root)
    def tester(self,l,r):
        if l is None and r is None:
            return True
        if l is None or r is None :
            return False
        return (l.val == r.val) and self.tester(l.right, r.left) and self.tester(l.left, r.right)
            
        
        
        