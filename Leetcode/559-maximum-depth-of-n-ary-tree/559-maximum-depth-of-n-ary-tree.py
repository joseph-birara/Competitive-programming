"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        d = 0
        if root.children:
            d = max(self.maxDepth(n) for n in root.children)
        return d+1
        
        