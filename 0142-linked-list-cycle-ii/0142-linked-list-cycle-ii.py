# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                while slow!=head:
                    slow=slow.next
                    head=head.next
                return head
        return None"""
        fast=slow=head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                break
        else :
            return None
        while slow!=head:
            slow=slow.next
            head=head.next
        return head
            
            