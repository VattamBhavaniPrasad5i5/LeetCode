# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution:
#     def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
#         pv=head
#         temp=head
#         temp=temp.next
#         while temp:
#             if temp.val==val:
#                 pv.next=temp.next
#             pv=temp
#             temp=temp.next
#         return head
class Solution:
    def removeElements(self, head, T):
        dummy = ListNode(-1, head)
        prev = dummy
        while head:
            if head.val != T:
                prev = head
            else:
                prev.next = head.next
            head = head.next
        return dummy.next