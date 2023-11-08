# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        left_sum = 0
        
        def add_left_leaf(root,left_right):
            nonlocal left_sum
            
            if root: 
                if not root.left and not root.right and left_right =="left" :
                    print(root.val)
                    left_sum += root.val
                add_left_leaf(root.left,"left")
                add_left_leaf(root.right,"right")
                
        add_left_leaf(root,"no")
        return left_sum
 