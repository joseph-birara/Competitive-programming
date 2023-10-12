# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:
        def postorder(node):
            if not node:
                return "null"  
            left = postorder(node.left)
            right = postorder(node.right)

            
            subtree = str(node.val) + "," + left + "," + right
            subtree_count[subtree] += 1

            if subtree_count[subtree] == 2:
                result.append(node)

            return subtree

        subtree_count = collections.defaultdict(int)
        result = []
        postorder(root)
        # print(subtree_count)
        return result

        
