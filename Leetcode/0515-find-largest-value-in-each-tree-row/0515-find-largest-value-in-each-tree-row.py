
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:  
            return []

        q = deque()
        q.append(root)
        ans = []

        while q:
            n = len(q)   
            localmax = float('-inf') 
            for _ in range(n):
                node = q.popleft()
                localmax = max(localmax, node.val)  
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            ans.append(localmax)
        
        return ans
