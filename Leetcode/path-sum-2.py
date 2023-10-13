# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        
        answer = []

        def backTrack(arr, node, sum_):
            if not node:
                return
            arr.append(node.val)
            sum_ += node.val

            if node.left == None and node.right == None:
                if sum_ == targetSum:
                    answer.append(arr.copy())
                # arr.pop()
                return 

            if node.left:
                backTrack(arr, node.left, sum_)
                arr.pop()
            if node.right:
                backTrack(arr, node.right, sum_)
                arr.pop()

        backTrack([], root, 0)
        return answer
