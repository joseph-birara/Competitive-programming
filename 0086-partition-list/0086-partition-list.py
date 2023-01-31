# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
      

   
        # Create two dummy heads for two linked lists
        less_head, less_tail = ListNode(0), ListNode(0)
        greater_head, greater_tail = ListNode(0), ListNode(0)
        # Create two pointers to traverse the linked lists
        less, greater = less_head, greater_head

        # Traverse the original linked list
        while head:
            # If the current node's value is less than x, add it to the less linked list
            if head.val < x:
                less.next = head
                less = less.next
            # If the current node's value is greater than or equal to x, add it to the greater linked list
            else:
                greater.next = head
                greater = greater.next
            # Move to the next node
            head = head.next

        # End the greater linked list
        greater.next = None
        # Join the two linked lists together
        less.next = greater_head.next

        # Return the head of the new linked list
        return less_head.next

        