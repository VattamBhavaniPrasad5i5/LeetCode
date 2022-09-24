class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        res = []

        def pathSumHelper(root, cur_path):
            if not root:
                return

            cur_path.append(root.val)
            if not root.left and not root.right and sum(cur_path) == targetSum:
                res.append(cur_path[:])

            pathSumHelper(root.left, cur_path)
            pathSumHelper(root.right, cur_path)
            cur_path.pop()

        pathSumHelper(root, [])
        return res
