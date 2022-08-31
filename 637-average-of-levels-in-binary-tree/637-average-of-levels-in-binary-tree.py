# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue
class Solution:
   
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Traversing level by level 
        res = []

        q = Queue()
        q.put(root) 
        while (not q.empty()):         
            Sum = 0
            count = 0
            temp = Queue() 
            while (not q.empty()): 
                n = q.queue[0] 
                q.get() 
                Sum += n.val 
                count += 1
                if (n.left != None):
                    temp.put(n.left) 
                if (n.right != None): 
                    temp.put(n.right)
            q = temp 
            res.append((Sum * 1.0 / count))
        return res

            
        
        