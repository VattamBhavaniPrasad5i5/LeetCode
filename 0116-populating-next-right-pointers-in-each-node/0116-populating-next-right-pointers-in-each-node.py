"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution(object):
    def connect(self, root):
        if not root: return root
        if root.left: 
            left, right = root.left, root.right
            self.connect(left)
            self.connect(right)
            while left:
                left.next = right
                left, right = left.right, right.left
        return root