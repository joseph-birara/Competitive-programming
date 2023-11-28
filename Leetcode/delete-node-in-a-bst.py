# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return  None
        elif root.val <key:
            root.right = self.deleteNode(root.right,key)
        elif root.val >key:
            root.left = self.deleteNode(root.left,key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            else:
                succesor = self.find_right_min(root.right)
                root.val = succesor
                root.right= self.deleteNode(root.right,succesor)
        return root
            
        
        
        
    # find the smallest element in the right sub tree
    def find_right_min(self,root):
        while root.left:
            root = root.left
        return root.val
    
        