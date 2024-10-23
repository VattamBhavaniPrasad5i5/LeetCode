# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def replaceValueInTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: Optional[TreeNode]
        """
        pq = deque()
        pq.append((root.val, root))
        
        while pq:
            n = len(pq)
            
			# calculate levelSum at each level
            levelSum = 0
            for localSum, node in pq:
                levelSum += node.val
                
            for i in range(n):
                localSum, node = pq.popleft()
                
				# calculate childSum
                childSum = 0
                if node.left: childSum += node.left.val
                if node.right: childSum += node.right.val
                
				# queue children with childSum
                if node.left: pq.append((childSum, node.left))
                if node.right: pq.append((childSum, node.right))
                   
				# new node value is levelSum - localSum
                node.val = levelSum - localSum
                 
        return root