# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        global res 
 

        def getSum(curr, p, gp):

            global res

            # Base condition
            if (curr == None):
                return

            if (gp != None and gp.val % 2 == 0):
                res += curr.val

            # Recurse for left child
            getSum(curr.left, curr, p)

            # Recurse for right child
            getSum(curr.right, curr, p)
        
        res = 0
        getSum(root,None,None)
        return res