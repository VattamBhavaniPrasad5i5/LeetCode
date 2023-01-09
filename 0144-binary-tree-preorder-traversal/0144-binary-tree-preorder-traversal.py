class Solution:
    def traversal(self, root, preorder):
        if root:
            preorder.append(root.val)
            self.traversal(root.left, preorder)
            self.traversal(root.right, preorder)
            
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        preorder = []
        self.traversal(root, preorder)
        return preorder