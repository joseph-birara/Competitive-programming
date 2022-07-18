# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        while(head):
            temp.append(head.val)
            head = head.next
        x = ListNode()
        y = x
        temp.reverse()
        for i in temp :
            y.next = ListNode(i)
            y = y.next
            

        
        return x.next
        
        