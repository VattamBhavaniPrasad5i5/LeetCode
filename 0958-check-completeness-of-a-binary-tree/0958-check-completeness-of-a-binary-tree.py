# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        have_null = False
        Q = [root]
        
        while Q:
            cur_node = Q.pop(0)
            if not cur_node: 
                have_null = True
                continue
            if have_null: return False
            Q.append(cur_node.left)
            Q.append(cur_node.right)
            
        return True