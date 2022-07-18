# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp = []
        
        x = ListNode()
        y = x
        while(list1):
            temp.append(list1.val)
            list1 = list1.next
        
            
        while list2:
            temp.append(list2.val)
            list2 = list2.next
       
        temp.sort()
        
        for i in temp:
            y.next= ListNode(i)
            y= y.next
        return x.next
            
            
        