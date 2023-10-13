# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root :
            return 0
        max_width = 0
        q = deque([(root, 0)])
        
        while q:
            level_size = len(q)
            left_index = q[0][1]
            right_index = q[-1][1]
            max_width = max(max_width, right_index - left_index + 1)
            
            for _ in range(level_size):
                node, index = q.popleft()
                
                if node.left:
                    q.append((node.left, 2*index+1))
                
                if node.right:
                    q.append((node.right, 2*index+2))
        
        return max_width







        
