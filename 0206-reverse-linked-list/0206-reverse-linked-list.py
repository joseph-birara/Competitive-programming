# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while head:
            temp.insert(0,head.val)
            head= head.next
        head= ListNode()
        y = head
        for element in temp:
            y.next = ListNode(element)
            y = y.next
        return head.next
            
            
            
        
            
        