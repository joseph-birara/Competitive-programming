# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = []
        for i in lists:
            k = i
            while k:
                temp.append(k.val)
                k = k.next
        heapify(temp)
        node = head = ListNode()
        n = len(temp)
        for i in range(n):
            newNode = ListNode(heappop(temp))
            node.next= newNode
            node = node.next
            
        return head.next
        
        