# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.d = defaultdict(int)
        if root:
            root.val = 0
            self.d[0] += 1
        def dfs(root):
            if not root:
                return
            if root and root.left:
                root.left.val = 2 * root.val +1
                self.d[root.left.val] += 1
            dfs(root.left)
            
            if root and root.right:
                root.right.val = 2 * root.val +2
                self.d[root.right.val] += 1
            dfs(root.right)
        dfs(root)
        

    def find(self, target: int) -> bool:
        if self.d[target]:
            return True
        return False
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)