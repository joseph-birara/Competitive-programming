"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        global res
        res = 0
        def findNode(k):
            for n in employees:
                if n.id == k:
                    return n
        def dfs(node):
            global res
            res += node.importance
            for i in node.subordinates:
                dfs(findNode(i))
        dfs(findNode(id))
        return res
            
            
        
        