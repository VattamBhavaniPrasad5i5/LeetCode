class Solution:
    def __init__(self, head):
        self.head = head

    def getRandom(self):
        n, k = 1, 1
        head, ans = self.head, self.head
        while head.next:
            n += 1
            head = head.next
            if random.random() < k/n:
                ans = ans.next
                k += 1
                
        return ans.val