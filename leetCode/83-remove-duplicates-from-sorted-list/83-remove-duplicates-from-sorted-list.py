# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        res = []
        while  head:
            c = head.val
            if c not in res:
                res.append( c)
            head =  head.next
        x = ListNode()
        y = x
        for i in res:
            y.next = ListNode(i)
            y = y.next
        return x.next
         
        