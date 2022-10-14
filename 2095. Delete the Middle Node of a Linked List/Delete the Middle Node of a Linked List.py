# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow=head
        fast=head
        if head.next:
            
            while fast and fast.next:
                prev=slow
                slow=slow.next
                fast=fast.next.next
            prev.next=slow.next
            return head
        else:
            return head.next
        
