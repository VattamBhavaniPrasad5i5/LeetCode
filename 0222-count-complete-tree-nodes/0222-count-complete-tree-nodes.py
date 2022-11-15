# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Path(self, root, num):
        for s in bin(num)[3:]:
            if s == "0": 
                root = root.left
            else:
                root = root.right
            if not root: return False
        return True
        
    def countNodes(self, root):
        if not root: return 0
        
        left, depth = root, 0
        while left.left:
            left, depth = left.left, depth + 1

        begin, end = (1<<depth), (1<<(depth+1)) - 1
        if self.Path(root,end): return end
        
        while begin + 1 < end:
            mid = (begin + end)//2
            if self.Path(root, mid):
                begin = mid
            else:
                end = mid
        return begin