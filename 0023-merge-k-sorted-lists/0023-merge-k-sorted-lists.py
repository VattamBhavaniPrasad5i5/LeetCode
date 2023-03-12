# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        arr = []
        for l in lists:
            while l:
                arr.append(l.val)
                l = l.next
        
        arr.sort()
        res = ListNode(0)
        rNext = res
        for d in arr:
            rNext.next = ListNode(d)
            rNext = rNext.next
            
        return res.next   