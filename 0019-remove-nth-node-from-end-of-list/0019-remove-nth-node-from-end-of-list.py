# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        leanth=0
        node=head
        while node:
            node,leanth=node.next,leanth+1
        node=head
        if leanth-n==0:
            return head.next
        count=0
        while node:
            count+=1
            if count==(leanth-n):
                print(node.val)
                node.next=node.next.next
            node=node.next
        return head