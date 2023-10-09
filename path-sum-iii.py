# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        pathCount = [0]

        def countPath(dct,curr_sum,node):
            if not node:
                return
            curr_sum += node.val 

            pathCount[0]+= dct[curr_sum-targetSum]
            dct[curr_sum] +=1
            countPath(dct,curr_sum,node.left)          
            countPath(dct,curr_sum,node.right)
            dct[curr_sum] -= 1

        countPath(defaultdict(int,{0:1}),0,root)

        return pathCount[0]
    
            

            



        
